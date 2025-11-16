# 🚀 Guía de Deploy en Vercel

## Pasos para Deployar ConsolidGPT en Vercel

### 1. Preparación

Asegúrate de tener una cuenta en [Vercel](https://vercel.com) (puedes usar tu cuenta de GitHub).

### 2. Instalar Vercel CLI (Opcional)

```bash
npm install -g vercel
```

### 3. Deploy desde la Terminal

**Opción A: Deploy con CLI**

```bash
# Desde la raíz del proyecto
vercel

# Sigue las instrucciones:
# - Set up and deploy? Yes
# - Which scope? (tu cuenta)
# - Link to existing project? No
# - Project name? consolid-gpt (o el que quieras)
# - Directory? ./
# - Override settings? No
```

**Opción B: Deploy desde GitHub**

1. Sube tu proyecto a GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - ConsolidGPT"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/consolid-gpt.git
   git push -u origin main
   ```

2. Ve a [vercel.com/new](https://vercel.com/new)
3. Importa tu repositorio de GitHub
4. Vercel detectará automáticamente la configuración
5. Click en "Deploy"

### 4. Configuración Automática

Vercel usará automáticamente:
- `vercel.json` para la configuración
- `requirements.txt` para las dependencias de Python
- `app.py` como punto de entrada

### 5. Variables de Entorno (IMPORTANTE)

**DEBES configurar la API key de Google en Vercel:**

En el dashboard de Vercel:
1. Ve a tu proyecto
2. Settings → Environment Variables
3. Agrega:
   - **Name:** `GOOGLE_API_KEY`
   - **Value:** `AIzaSyC5UAimCkhMrdWZ12YrI4chzchSfwQBbJY` (o tu propia key)
   - **Environment:** Production, Preview, Development
4. Click "Save"
5. Redeploy tu proyecto para que tome efecto

### 6. URL de Producción

Después del deploy, Vercel te dará una URL como:
```
https://consolid-gpt-xxxxx.vercel.app
```

### 7. Dominio Personalizado (Opcional)

1. Ve a Settings → Domains
2. Agrega tu dominio personalizado
3. Configura los DNS según las instrucciones

## 🔧 Comandos Útiles

```bash
# Deploy a producción
vercel --prod

# Ver logs
vercel logs

# Ver lista de deployments
vercel ls

# Remover proyecto
vercel remove consolid-gpt
```

## 📝 Notas Importantes

- **Límites de Vercel Free Tier:**
  - 100 GB de ancho de banda/mes
  - Funciones serverless con timeout de 10s
  - Suficiente para un chatbot como ConsolidGPT

- **Actualizaciones:**
  - Si usas GitHub, cada push a `main` desplegará automáticamente
  - Si usas CLI, ejecuta `vercel --prod` para actualizar

- **Base de Datos:**
  - Actualmente usa archivo .txt (funciona en Vercel)
  - Para escalar, considera migrar a una base de datos externa

## 🐛 Troubleshooting

**Error: "Module not found"**
- Verifica que todas las dependencias estén en `requirements.txt`

**Error: "Build failed"**
- Revisa los logs en el dashboard de Vercel
- Asegúrate de que `vercel.json` esté configurado correctamente

**La app no carga:**
- Verifica que `app.py` esté en la raíz del proyecto
- Revisa los logs con `vercel logs`

## 🎉 ¡Listo!

Tu ConsolidGPT estará disponible en línea para que tus clientes lo usen desde cualquier lugar.
