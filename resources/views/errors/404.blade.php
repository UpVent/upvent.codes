<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>¡Oops! Algo salió mal :(</title>


        @include('includes.head-static')
    </head>
    <body>
        <div class="min-w-screen min-h-screen bg-blue-100 flex items-center p-5 lg:p-20 overflow-hidden relative">
            <div class="flex-1 min-h-full min-w-full rounded-3xl bg-white shadow-xl p-10 lg:p-20 text-gray-800 relative md:flex items-center text-center md:text-left">
                <div class="w-full md:w-1/2">
                    <div class="mb-10 lg:mb-20">
                        <img class="object-center object-contain h-10 w-15" src="{{asset('img/logo-grey.png')}}" alt="UpVent White Logo" />
                    </div>
                    <div class="mb-10 md:mb-20 text-gray-600 font-light">
                        <h1 class="font-black uppercase text-3xl lg:text-5xl text-blue-500 mb-10">¡Es peligroso ir solo!</h1>
                        <p>La página que buscas no está disponible o ha sido eliminada.</p>
                        <p>Intenta buscar de nuevo o regresa al inicio con el botón de abajo.</p>
                        <p>Si crees que se trata de un error contacta a:</p>
                        <p class="text-gray-900 italic">
                            webmaster@upvent.codes
                        </p>
                    </div>
                    <div class="mb-20 md:mb-0">
                        <button class="text-lg font-light outline-none focus:outline-none transform transition-all hover:scale-110 text-blue-500 hover:text-blue-600"><i class="bi bi-arrow-left m-3"></i><a href="{{url('/')}}">Regresar</a></button>
                    </div>
                </div>
                <div class="w-full md:w-1/2 text-center">
                    <img class="animate-bounce object-center object-contain" src="{{asset('img/error-404.svg')}}" alt="UpVent White Logo" />
                </div>
            </div>
        </div>
    </body>
</html>
