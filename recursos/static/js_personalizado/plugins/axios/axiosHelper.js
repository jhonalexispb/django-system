
const tiempoEstandar = { timeout: 15000 };

const handleResponse = (response) => {
    return response.data;
};

const handleError = (error,nombre,formulario) => {
    let errorMessage = "¡Ups! Algo salió mal. Por favor, inténtalo de nuevo.";
    let errorIcon = '/static/media/gif/error_de_conexion.json' ;
    let lottieContainer = '<div id="lottie-container" style="width: 200px; height: 200px; margin: 0 auto;"></div>';

    if (error.response) {
        switch (error.response.status) {
            case 400:
                errorMessage = `Error ${error.response.status}: Parece que hubo un error en la solicitud.`;
                errorIcon = '/static/media/gif/error_400.json' ;
                break;
            case 404:
                errorMessage = `Error ${error.response.status}: ¡Vaya! No encontramos lo que buscabas.`;
                errorIcon = '/static/media/gif/error_404.json';
                console.log(errorIcon)
                break;
            case 422: // Errores de validación
                clearErrors(formulario);
                const form = document.getElementById(formulario);
                const errors = error.response.data.errors;
                let errorMessages = [];
                
                for (const field in errors) {
                    const errorMessage = errors[field][0];
                    const input = form.querySelector(`[name="${field}"]`);
                    if(input){
                        input.classList.add('is-invalid');
                        const errorDiv = document.createElement('span');
                        errorDiv.className = 'error text-danger';
                        errorDiv.textContent = errorMessage;
                        input.parentNode.insertBefore(errorDiv, input.nextSibling);
                    }
                }

                if (error.response.data.error) {
                    errorMessages.push(error.response.data.error);
                    errorMessage = `${nombre}, ${errorMessages.join(', ')}, verifica los datos por favor :)`;
                    errorIcon = '/static/media/gif/alerta.json' ;
                } else {
                    errorMessage = `${nombre}, encontramos errores en tu formulario, verifica los datos por favor :)`;
                    errorIcon = '/static/media/gif/formulario_invalido.json' ;
                }
                break;
            case 401:
            case 419:
                window.location.href = '/login';
                return;
            case 500:
                errorMessage = "Hay un problema con el servidor. Estamos trabajando para solucionarlo.";
                errorIcon = '/static/media/gif/error_500.json' ;
                break;
            default:
                errorMessage = `Error ${error.response.status}: Ocurrió un problema inesperado.`;
                errorIcon = '/static/media/gif/error_de_conexion.json' ;
        }
    } else if (error.request) {
        errorMessage = "La conexión está tardando más de lo esperado. Por favor, verifica tu conexión a Internet.";
        errorIcon = '/static/media/gif/carga_lenta.json' ;
    } else {
        errorMessage = "Hubo un problema al configurar la solicitud: " + error.message;
    }

    Swal.fire({
        title: "¡Oops!",
        html: `${lottieContainer} <br> ${errorMessage}`,
        showCloseButton: true,
        backdrop: true,
        didOpen: () => {
            // Aquí es donde se carga la animación Lottie dentro del contenedor cuando se abre SweetAlert
            lottie.loadAnimation({
                container: document.getElementById('lottie-container'),  // El contenedor donde se va a renderizar la animación
                renderer: 'svg',
                loop: true,  // Hacer que la animación se repita
                autoplay: true,  // Reproducir automáticamente la animación
                path: errorIcon  // Ruta a la animación de Lottie
            });
        },
        didRender: () => {
            // Ajustamos los estilos para evitar el scroll vertical no deseado
            const swalHtmlContainer = document.querySelector('.swal2-html-container');
            if (swalHtmlContainer) {
                swalHtmlContainer.style.maxHeight = 'none';  // Eliminar la restricción de altura
                swalHtmlContainer.style.overflow = 'visible';  // Evitar el overflow que genera el scroll
            }
        }
    });
};

function clearErrors(formulario) {
    const form = document.getElementById(formulario);
    const errorMessages = form.querySelectorAll('span.error');
    const inputError = form.querySelectorAll('input.is-invalid')
    errorMessages.forEach((msg) => {
        msg.remove();
    });
    inputError.forEach((error) => {
        error.classList.remove('is-invalid');
    })
}

export { handleResponse, handleError, tiempoEstandar, clearErrors};