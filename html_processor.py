"""
HTML Processor - Base class for HTML file processing
Provides common functionality for reading, modifying, and writing HTML files
"""

import re
from pathlib import Path
from typing import Callable, Optional, Dict, Any


class HTMLProcessor:
    """Base class for processing HTML files with common patterns"""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize HTML processor
        
        Args:
            base_dir: Base directory for file operations (defaults to current working directory)
        """
        self.base_dir = base_dir or Path.cwd()
    
    def process_file(self, file_path: Path, 
                    processor_func: Callable[[str], str],
                    encoding: str = 'utf-8') -> tuple[bool, str]:
        """
        Process individual HTML file with a custom processor function
        
        Args:
            file_path: Path to the HTML file
            processor_func: Function that takes HTML content and returns modified content
            encoding: File encoding (default: utf-8)
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
            
            # Apply custom processing
            modified_content = processor_func(content)
            
            # Only write if content changed
            if modified_content != content:
                with open(file_path, 'w', encoding=encoding) as f:
                    f.write(modified_content)
                return True, f"Modified: {file_path.name}"
            else:
                return True, f"No changes: {file_path.name}"
                
        except Exception as e:
            return False, f"Error processing {file_path.name}: {e}"
    
    def process_files(self, 
                     file_pattern: str = '*.html',
                     processor_func: Optional[Callable[[str], str]] = None,
                     directories: Optional[list[Path]] = None,
                     encoding: str = 'utf-8') -> Dict[str, Any]:
        """
        Process multiple HTML files with a custom processor function
        
        Args:
            file_pattern: Glob pattern for matching files (default: *.html)
            processor_func: Function that takes HTML content and returns modified content
            directories: List of directories to process (default: base_dir)
            encoding: File encoding (default: utf-8)
            
        Returns:
            Dictionary with processing statistics
        """
        if directories is None:
            directories = [self.base_dir]
        
        all_files = []
        for directory in directories:
            if directory.exists():
                all_files.extend(directory.glob(file_pattern))
        
        stats = {
            'total_files': len(all_files),
            'processed': 0,
            'modified': 0,
            'errors': 0,
            'error_details': []
        }
        
        for file_path in all_files:
            if processor_func:
                success, message = self.process_file(file_path, processor_func, encoding)
                stats['processed'] += 1
                
                if success:
                    if 'Modified' in message:
                        stats['modified'] += 1
                    print(f"  {message}")
                else:
                    stats['errors'] += 1
                    stats['error_details'].append(message)
                    print(f"  {message}")
        
        return stats
    
    def find_and_replace(self, 
                        html_content: str, 
                        pattern: str, 
                        replacement: str,
                        flags: int = 0) -> str:
        """
        Find and replace pattern in HTML content
        
        Args:
            html_content: HTML content to process
            pattern: Regex pattern to find
            replacement: Replacement string (can use backreferences)
            flags: Regex flags (default: 0)
            
        Returns:
            Modified HTML content
        """
        return re.sub(pattern, replacement, html_content, flags=flags)
    
    def insert_after_pattern(self,
                           html_content: str,
                           pattern: str,
                           content_to_insert: str,
                           flags: int = 0) -> str:
        """
        Insert content after a matching pattern in HTML
        
        Args:
            html_content: HTML content to process
            pattern: Regex pattern to find
            content_to_insert: Content to insert after the pattern
            flags: Regex flags (default: 0)
            
        Returns:
            Modified HTML content
        """
        def replacer(match):
            return match.group(0) + content_to_insert
        
        return re.sub(pattern, replacer, html_content, count=1, flags=flags)
    
    def insert_before_pattern(self,
                            html_content: str,
                            pattern: str,
                            content_to_insert: str,
                            flags: int = 0) -> str:
        """
        Insert content before a matching pattern in HTML
        
        Args:
            html_content: HTML content to process
            pattern: Regex pattern to find
            content_to_insert: Content to insert before the pattern
            flags: Regex flags (default: 0)
            
        Returns:
            Modified HTML content
        """
        def replacer(match):
            return content_to_insert + match.group(0)
        
        return re.sub(pattern, replacer, html_content, count=1, flags=flags)
    
    def check_pattern_exists(self, html_content: str, pattern: str, flags: int = 0) -> bool:
        """
        Check if a pattern exists in HTML content
        
        Args:
            html_content: HTML content to check
            pattern: Regex pattern to search for
            flags: Regex flags (default: 0)
            
        Returns:
            True if pattern exists, False otherwise
        """
        return bool(re.search(pattern, html_content, flags=flags))