#### ACTUALIZAR GIT
No se necesita actualizar Git en Windows, siempre se ejecuta la version mas nueva desde el sitio oficial.

### CONFIGURAR USUARIO

*Nombre de usuario*
```shell
git config --global user.name "Nombre"
```

*Correo electrónico*
```shell
git config --global user.email "email"
```

*Revisar configuraciones*
```shell
git config --list
```

### CREAR LLAVE SSH
Una llave SSH sirve para conectarte de forma segura a tus repositorios remotos, permitiendo la autenticación automática y sin contraseña en cada operación de Git.

1. *Revisar si ya existen llaves SSH*
> Desde la consola git Bash o CMD
```shell
ls ~/.ssh
```
Si existen archivos `id_ras.pub` o `id_ed25519.pub`, ya existen llaves creadas (Saltar al paso 6), caso contrario, generar una nueva

2. *Generar nueva llave SSH*
> Se puede utilizar `ras` o `ed25519`,
```shell
ssh-keygen -t ras -C "emailusuario@ejemplo.com"
```
Cuando pregunte por ubicación, solo presionar enter para utilizar la ubicación determinada. Igual se puede omitir el uso de contraseña al dejar el campo vacío cuando la pida.

3. *Añadir la llave SSH a GitHub*
Copiar de la terminal la SSH pública
```shell
cat ~/.ssh/id_ras.pub
```
Abrir GitHub en el navegador y entrar a `Configuraciones` -> `SSH adn GPG keys` -> `New SSH key`, poner título descriptivo y pegar la llave pública. Guardarla con `Add SSH key`.

4. *Probar la conexión del SSH en GitHub*
```shell
ssh -T git@github.com
```
La primera vez aparecerá un mensaje de confirmación, se tiene confirmar con `yes`. Si la conexión fue exitosa, aparecerá un mensaje de bienvenida. ✅

### COMANDOS BIEN DESCRITOS
https://ealcaraz85.github.io/Graficacion.io/#org96e7092

