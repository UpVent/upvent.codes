<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>{{config('app.name', 'UpVent')}} - Acerca De.</title>

        @include('includes.head-static')

    </head>
    <body class="antialiased font-montserrat">
        <div class="shadow-xl">
            <nav class=" flex items-center justify-between flex-wrap bg-upvent p-6">
                <!-- Navbar Logo -->
                <div class="flex items-center flex-no-shrink mr-6">
                    <img class="object-center object-contain h-10 w-15" src="{{asset('img/logo-white.png')}}" alt="UpVent White Logo" />
                </div>
                <!-- Menu hidden -->
                <div class="block lg:hidden">
                    <button data-toggle-hide="[data-nav-content]" class="flex items-center px-3 py-2 border rounded text-white border-teal-light hover:text-white hover:border-white rounded focus:outline-none focus:shadow-outline">
                        <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <title>
                                Menu
                            </title>
                            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                        </svg>
                    </button>
                </div>

                <!-- Menu shown -->
                <div data-nav-content="" class="w-full block flex-grow lg:flex lg:items-center lg:w-auto hidden lg:block">
                    <div class="text-sm text-white lg:flex-grow">

                        <a class="block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline" href="#responsive-header">
                            Inicio
                        </a>

                        <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Blog
                        </a>

                        <a href="#responsive-header" class="block text-black rounded-lg bg-white shadow-lg p-2 mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-blue mr-4 rounded focus:outline-none focus:shadow-outline">
                            Nosotros
                        </a>

                        <a href="#responsive-header" class=" block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Servicios
                        </a>

                        <a href="#responsive-header" class=" block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Contacto
                        </a>

                        <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Marketcloud
                        </a>

                        @if (Route::has('login'))
                            @auth
                            <a href="{{ url('/dashboard') }}" class="block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                                Panel de Administración <i class="bi bi-speedometer2"></i>
                            </a>
                        @else
                            <a href="{{ route('login') }}" class="block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                                Login <i class="bi bi-person-circle"></i>
                            </a>
                            @if (Route::has('register'))
                                <a href="{{ route('register') }}" class="block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                                    Registro <i class="bi bi-pencil-square"></i>
                                </a>
                            @endif
                            @endauth
                        @endif
                    </div>
                    <div class="text-white lg:w-64 pl-8 flex-shrink-0 flex items-center justify-end space-x-6">
                        <a href="https://github.com/UpVent"><i class="bi bi-github"></i></a>
                        <a href="https://www.facebook.com/UpVentMX"><i class="bi bi-facebook"></i></a>
                        <a href="https://www.instagram.com/upventmx"><i class="bi bi-instagram"></i></a>
                        <a href="mailto:upventmx@gmail.com?subject=Contacto%20desde%20p%C3%A1gina%20web"><i class="bi bi-envelope-fill"></i></a>
                    </div>
                </div>
            </nav>
        </div>

        <!-- Jumbotron -->
        <div class="relative bg-white overflow-hidden">
            <div class="max-w-7xl mx-auto">
                <div class="relative z-10 pb-8 bg-white sm:pb-16 md:pb-20 lg:max-w-2xl lg:w-full lg:pb-28 xl:pb-32">
                    <main class="mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
                        <div class="sm:text-center lg:text-center">
                            <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
                                <span class="block text-upvent xl:inline">Nosotros</span>
                            </h1>
                            <p class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                                Llevando empresas a la nube desde nuestros inicios.
                            </p>

                            <p class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                                UpVent es una compañía de tecnología y software empresarial que sigue el modelo del software libre enfocado a las micro, pequeñas y medianas empresas Mexicanas.
                            </p>
                        </div>
                    </main>
                </div>
            </div>
            <div class="sm:hidden md:inline-flex lg:inline-flex p-4 lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
                <img class="rounded-lg object-center object-contain h-5/6 w-4/6" src="{{asset('img/about-us.svg')}}" alt="">
            </div>
        </div>

        <hr />

        <!-- Values -->
        <div class="sm:text-center md:text-center lg:text-center">
            <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
                Nuestros valores, y algo más...
            </p>
            <p class="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
                Conozca los tres pilares que hacen UpVent una realidad. Nuestros valores son fundamento de nuestra empresa y gracias a ellos podemos brindarle productos éticos en todo momento y en todo lugar.
            </p>
        </div>

        <div class="sm:flex flex-wrap justify-center items-center text-center gap-4">
            <div class="w-full sm:w-1/2 md:w-1/2 lg:w-1/4 px-4 py-4 bg-white mt-6  shadow-lg rounded-lg dark:bg-gray-800">
                <div class="flex-shrink-0">
                    <div class="flex items-center mx-auto justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                        <i class="bi bi-book-fill"></i>
                    </div>
                </div>
                <h3 class="text-2xl sm:text-xl text-gray-700 font-semibold dark:text-white py-4">
                    Educación
                </h3>
                <p class="text-md  text-gray-500 dark:text-gray-300 py-4">
                    Compartir el conocimiento es uno de los valores que fundó UpVent. Por ello procuramos liberar, compartir y escribir tutoriales actualizados de tecnología para retribuir a nuestra comunidad.
                </p>
            </div>

            <div class="w-full sm:w-1/2 md:w-1/2 lg:w-1/4 px-4 py-4 mt-6 sm:mt-16 md:mt-20 lg:mt-24 bg-white shadow-lg rounded-lg dark:bg-gray-800">
                <div class="flex-shrink-0">
                    <div class="flex items-center mx-auto justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                        <i class="bi bi-graph-up"></i>
                    </div>
                </div>
                <h3 class="text-2xl sm:text-xl text-gray-700 font-semibold dark:text-white py-4">
                    Crecimiento
                </h3>
                <p class="text-md text-gray-500 dark:text-gray-300 py-4">
                    Al ser entusiastas de la cultura DevOps nos gusta construir software escalable, modular y manejable para nuestros clientes. Siempre escalable, siempre seguro, siempre eficiente.
                </p>
            </div>

            <div class="w-full sm:w-1/2 md:w-1/2 lg:w-1/4 mt-6  px-4 py-4 bg-white shadow-lg rounded-lg dark:bg-gray-800">
                <div class="flex-shrink-0">
                    <div class="flex items-center mx-auto justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                        <i class="bi bi-star-fill"></i>
                    </div>
                </div>
                <h3 class="text-2xl sm:text-xl text-gray-700 font-semibold dark:text-white py-4">
                    Ética
                </h3>
                <p class="text-md  text-gray-500 dark:text-gray-300 py-4">
                    No vendemos, intercambiamos ni liberamos los datos de nuestros clientes. Toda tu información es confidencial y todo nuestro software vendido cumple con las licencias que respetan tu libertad.
                </p>
            </div>

        </div>



        <!-- Footer -->
        @include('includes.footer')

        <!-- Scripts -->
        <script src="/js/app.js" type="text/javascript"></script>
    </body>
</html>
