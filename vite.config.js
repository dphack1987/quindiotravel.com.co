import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy';
import { visualizer } from 'rollup-plugin-visualizer';
import { resolve } from 'path';

export default defineConfig(({ mode }) => ({
  // Configuración base para sitio estático multi-page
  root: '.',
  publicDir: 'assets',
  
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    
    // Preservar estructura de directorios para HTML
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        // Vite detectará automáticamente otros archivos HTML
      },
      output: {
        // Preservar estructura de assets
        assetFileNames: (assetInfo) => {
          const folders = {
            css: 'assets/css',
            js: 'assets/js',
            images: 'assets/images',
            videos: 'assets/videos',
            data: 'assets/data'
          };
          
          const extType = assetInfo.name.split('.').at(1);
          if (extType && folders[extType]) {
            return `${folders[extType]}/[name].[hash][extname]`;
          }
          return 'assets/[name].[hash][extname]';
        },
        chunkFileNames: 'assets/js/[name].[hash].js',
        entryFileNames: 'assets/js/[name].[hash].js',
      },
    },
    
    // Optimización
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: mode === 'production',
        drop_debugger: mode === 'production',
      },
      format: {
        comments: false,
      },
    },
    
    // Source maps para desarrollo
    sourcemap: mode === 'development',
    
    // Tamaño de chunk
    chunkSizeWarningLimit: 1000,
    
    // Copiar archivos estáticos que no necesitan procesamiento
    copyPublicDir: true,
  },
  
  // Plugins
  plugins: [
    // Copiar archivos estáticos adicionales
    viteStaticCopy({
      targets: [
        {
          src: 'assets/images',
          dest: 'assets/images'
        },
        {
          src: 'assets/videos',
          dest: 'assets/videos'
        },
        {
          src: 'assets/data',
          dest: 'assets/data'
        },
        {
          src: 'don-chucho-backend',
          dest: 'don-chucho-backend'
        },
        {
          src: 'pseo-engine',
          dest: 'pseo-engine'
        },
        {
          src: 'competitive-engine',
          dest: 'competitive-engine'
        },
        {
          src: '*.py',
          dest: '.'
        },
        {
          src: '*.js',
          dest: '.'
        },
      ]
    }),
    
    // Analizador de bundle (solo en modo analyze)
    mode === 'analyze' && visualizer({
      open: true,
      gzipSize: true,
      brotliSize: true,
    })
  ].filter(Boolean),
  
  // Configuración del servidor de desarrollo
  server: {
    port: 3000,
    open: true,
    cors: true,
  },
  
  // Optimización de dependencias
  optimizeDeps: {
    include: [],
  },
}));