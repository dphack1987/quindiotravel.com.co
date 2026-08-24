"""
Audit Utils - Common functions for HTML auditing and validation
Provides reusable functionality for website audits
"""

import re
from pathlib import Path
from typing import Dict, List, Any, Callable
from collections import defaultdict


def audit_html_elements(file_path: Path, 
                        element_pattern: str,
                        validator_func: Callable[[str], Dict[str, Any]],
                        encoding: str = 'utf-8') -> Dict[str, Any]:
    """
    Generic function to audit HTML elements in a file
    
    Args:
        file_path: Path to the HTML file
        element_pattern: Regex pattern to find elements
        validator_func: Function that validates each element and returns analysis dict
        encoding: File encoding (default: utf-8)
        
    Returns:
        Dictionary with audit results
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
        
        # Find all matching elements
        elements = re.findall(element_pattern, content, re.IGNORECASE)
        
        if not elements:
            return {
                'file': file_path.name,
                'total_elements': 0,
                'valid_elements': 0,
                'invalid_elements': 0,
                'issues': []
            }
        
        valid_count = 0
        invalid_count = 0
        all_issues = []
        
        for element in elements:
            analysis = validator_func(element)
            if analysis.get('valid', False):
                valid_count += 1
            else:
                invalid_count += 1
                if analysis.get('issue'):
                    all_issues.append(analysis['issue'])
        
        # Generate issue summary
        issue_summary = []
        if invalid_count > 0:
            # Count unique issues
            issue_counts = defaultdict(int)
            for issue in all_issues:
                issue_counts[issue] += 1
            issue_summary = [f"{count} {issue}" for issue, count in issue_counts.items()]
        
        return {
            'file': file_path.name,
            'total_elements': len(elements),
            'valid_elements': valid_count,
            'invalid_elements': invalid_count,
            'valid_percentage': (valid_count / len(elements) * 100) if elements else 0,
            'issues': issue_summary
        }
        
    except Exception as e:
        return {
            'file': file_path.name,
            'total_elements': 0,
            'valid_elements': 0,
            'invalid_elements': 0,
            'valid_percentage': 0,
            'issues': [f'Error de lectura: {e}']
        }


def analyze_directory(directory_path: Path,
                     element_pattern: str,
                     validator_func: Callable[[str], Dict[str, Any]],
                     file_pattern: str = '*.html',
                     encoding: str = 'utf-8') -> List[Dict[str, Any]]:
    """
    Analyze all HTML files in a directory for specific elements
    
    Args:
        directory_path: Path to the directory
        element_pattern: Regex pattern to find elements
        validator_func: Function that validates each element
        file_pattern: Glob pattern for HTML files (default: *.html)
        encoding: File encoding (default: utf-8)
        
    Returns:
        List of audit results for each file
    """
    dir_path = Path(directory_path)
    
    if not dir_path.exists():
        print(f"Directorio no encontrado: {directory_path}")
        return []
    
    html_files = list(dir_path.glob(file_pattern))
    
    if not html_files:
        print(f"No hay archivos HTML en: {directory_path}")
        return []
    
    print(f"\nAnalizando {len(html_files)} archivos en {directory_path}:")
    
    analyses = []
    for html_file in html_files:
        analysis = audit_html_elements(html_file, element_pattern, validator_func, encoding)
        analyses.append(analysis)
        
        if analysis['issues']:
            print(f"  - {analysis['file']}: {', '.join(analysis['issues'])} ({analysis['total_elements']} elementos)")
        else:
            print(f"  + {analysis['file']}: OK ({analysis['total_elements']} elementos)")
    
    return analyses


def generate_audit_summary(all_analyses: List[Dict[str, Any]], element_name: str = "elementos") -> Dict[str, Any]:
    """
    Generate summary statistics from audit analyses
    
    Args:
        all_analyses: List of audit result dictionaries
        element_name: Name of the elements being audited (default: "elementos")
        
    Returns:
        Dictionary with summary statistics
    """
    total_files = len(all_analyses)
    total_elements = sum(a['total_elements'] for a in all_analyses)
    total_valid = sum(a['valid_elements'] for a in all_analyses)
    total_invalid = sum(a['invalid_elements'] for a in all_analyses)
    files_with_issues = sum(1 for a in all_analyses if a['issues'])
    
    return {
        'total_files': total_files,
        f'total_{element_name}': total_elements,
        f'total_valid_{element_name}': total_valid,
        f'total_invalid_{element_name}': total_invalid,
        'files_with_issues': files_with_issues,
        'valid_percentage': (total_valid / total_elements * 100) if total_elements > 0 else 0
    }


def print_audit_report(summary: Dict[str, Any], 
                      all_analyses: List[Dict[str, Any]],
                      element_name: str = "elementos",
                      title: str = "AUDITORÍA") -> None:
    """
    Print a formatted audit report
    
    Args:
        summary: Summary statistics dictionary
        all_analyses: List of all audit analyses
        element_name: Name of elements being audited
        title: Report title
    """
    print("\n" + "=" * 60)
    print(f"RESUMEN DE {title}")
    print("=" * 60)
    print(f"Total archivos analizados: {summary['total_files']}")
    print(f"Total {element_name}: {summary[f'total_{element_name}']}")
    print(f"{element_name.capitalize()} válidos: {summary[f'total_valid_{element_name}']} ({summary['valid_percentage']:.1f}%)")
    print(f"{element_name.capitalize()} inválidos: {summary[f'total_invalid_{element_name}']}")
    print(f"Archivos con problemas: {summary['files_with_issues']}")
    
    # Show files with problems
    files_with_problems = [a for a in all_analyses if a['issues']]
    if files_with_problems:
        print("\nARCHIVOS CON PROBLEMAS:")
        for analysis in files_with_problems:
            print(f"  - {analysis['file']}: {', '.join(analysis['issues'])} ({analysis['total_elements']} {element_name})")


# Specific validators for common audit cases

def validate_alt_text(img_tag: str) -> Dict[str, Any]:
    """
    Validator for image alt text
    
    Args:
        img_tag: HTML img tag
        
    Returns:
        Dictionary with validation result
    """
    alt_match = re.search(r'alt=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
    
    if alt_match:
        alt_text = alt_match.group(1)
        if alt_text:  # If has content
            return {'valid': True, 'issue': None}
        else:  # If empty alt=""
            return {'valid': False, 'issue': 'Alt vacio'}
    else:
        return {'valid': False, 'issue': 'Sin alt'}


def validate_heading_structure(heading_tag: str) -> Dict[str, Any]:
    """
    Validator for heading structure
    
    Args:
        heading_tag: HTML heading tag
        
    Returns:
        Dictionary with validation result
    """
    # Check if heading has content
    content_match = re.search(r'<h[1-6][^>]*>(.*?)</h[1-6]>', heading_tag, re.IGNORECASE | re.DOTALL)
    if content_match:
        content = content_match.group(1).strip()
        if content:
            return {'valid': True, 'issue': None}
        else:
            return {'valid': False, 'issue': 'Heading vacio'}
    else:
        return {'valid': False, 'issue': 'Estructura invalida'}


def validate_meta_description(meta_tag: str) -> Dict[str, Any]:
    """
    Validator for meta description
    
    Args:
        meta_tag: HTML meta tag
        
    Returns:
        Dictionary with validation result
    """
    content_match = re.search(r'content=["\']([^"\']*)["\']', meta_tag, re.IGNORECASE)
    if content_match:
        content = content_match.group(1)
        if len(content) >= 50 and len(content) <= 160:
            return {'valid': True, 'issue': None}
        elif len(content) < 50:
            return {'valid': False, 'issue': 'Descripcion muy corta'}
        else:
            return {'valid': False, 'issue': 'Descripcion muy larga'}
    else:
        return {'valid': False, 'issue': 'Sin contenido'}