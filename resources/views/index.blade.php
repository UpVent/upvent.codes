<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>{{config('app.name', 'UpVent')}} - Soluciones en la nube para tu negocio. Low Cost, Siempre Listas.</title>


        @include('includes.head-static')

    </head>
    <body class="antialiased font-montserrat">
        <!-- This example requires Tailwind CSS v2.0+ -->
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

                        <a class="block text-black rounded-lg bg-white shadow-lg p-2 mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-blue mr-4 rounded focus:outline-none focus:shadow-outline" href="#responsive-header">
                            Inicio
                        </a>

                        <a href="#responsive-header" class=" block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Blog
                        </a>

                        <a href="#responsive-header" class=" block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
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

        <!-- Beta banner -->
        @include('includes.notice-banner')


        <!-- Jumbotron -->
        <div class="relative bg-white overflow-hidden">
            <div class="max-w-7xl mx-auto">
                <div class="relative z-10 pb-8 bg-white sm:pb-16 md:pb-20 lg:max-w-2xl lg:w-full lg:pb-28 xl:pb-32">
                    <main class="mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
                        <div class="sm:text-center lg:text-center">
                            <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
                                <span class="block xl:inline">Nube Inteligente, para negocios</span>
                                <span class="block text-upvent xl:inline">Inteligentes.</span>
                            </h1>
                            <p class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                                Líder Mexicano en desarrollo de soluciones empresariales de código libre.
                            </p>
                            <div class="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start">
                                <div class="rounded-md shadow">
                                    <a href="#" class="shadow-lg w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-upvent hover:bg-blue-800 md:py-4 md:text-lg md:px-10">
                                        Conocer más  <i class="bi bi-forward px-1"></i>
                                    </a>
                                </div>
                                <div class="mt-3 sm:mt-0 sm:ml-3">
                                    <a href="#" class="shadow-lg w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-blue-700 bg-blue-100 hover:bg-blue-200 md:py-4 md:text-lg md:px-10">
                                        Portafolio  <i class="bi bi-briefcase px-1"></i></i>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </main>
                </div>
            </div>
            <div class="sm:hidden md:inline-flex lg:inline-flex p-4 lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
                <img class="rounded-lg object-center object-contain h-5/6 w-4/6" src="{{asset('img/coworkers.svg')}}" alt="">
            </div>
        </div>

        <hr />

        <!-- Features section -->
        <div class="content-center mt-8">
            <div class="text-4xl text-center text-black">
                <h1>
                    Soluciones en la nube.
                    <br />
                    Para todo tipo de negocios.
                </h1>
                <p class="mt-8 text-sm text-gray-500 text-center">
                    Entusiastas, Desarrolladores y Empresas.
                    <br />
                    Todos tienen espacio en la nube con UpVent.
                </p>

                <!-- Features -->
                <div>
                    <div class="max-w-6xl mx-auto px-5 py-24 ">
                        <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4">
                            <div class="p-8 md:w-1/3 md:mb-0 mb-6 flex flex-col">
                                <div class="gray-light">
                                    <div class="rounded-lg shadow-lg p-4 transform translate-x-6 -translate-y-6">
                                        <div class="w-10 h-10 inline-flex text-upvent mb-5 flex-shrink-0 p-2">
                                            <i class="bi bi-laptop"></i>
                                        </div>
                                        <div class="flex-grow">
                                            <h2 class="text-xl title-font font-bold mb-3">Universales</h2>
                                            <p class="leading-relaxed text-sm text-center text-gray-500">
                                                Desarrollo profesional y universal. Cualquier plataforma, cualquier dispositivo. Donde sea.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="p-8 md:w-1/3 md:mb-0 mb-6 flex flex-col">
                                <div class="gray-light">
                                    <div class="rounded-lg shadow-lg p-4 transform translate-x-6 -translate-y-6"  >
                                        <div class="w-10 h-10 inline-flex text-upvent mb-5 flex-shrink-0 p-2">
                                            <i class="bi bi-bar-chart-line-fill"></i>
                                        </div>
                                        <div class="flex-grow">
                                            <h2 class="text-xl title-font font-bold mb-3">Escalables</h2>
                                            <p class="leading-relaxed text-sm text-center text-gray-500">
                                                Software escalable desde el primer día. Desde un pequeño sitio web hasta una plataforma corporativa.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="p-8 md:w-1/3 md:mb-0 mb-6 flex flex-col">
                                <div class="gray-light">
                                    <div class="rounded-lg shadow-lg p-4 transform translate-x-6 -translate-y-6"  >
                                        <div class="w-10 h-10 inline-flex text-upvent mb-5 flex-shrink-0 p-2">
                                            <i class="bi bi-unlock"></i>
                                        </div>
                                        <div class="flex-grow">
                                            <h2 class="text-xl title-font font-bold mb-3">Libres</h2>
                                            <p class="leading-relaxed text-sm text-center text-gray-500">
                                                Todas las soluciones empresariales de UpVent serán cien por ciento software libre.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>


                    <!-- Marketcloud shortcut -->
                    <div class="grid grid-cols-2 gap-4">
                        <div class="p-5 m-5">
                            <img class="object-contain" src="{{asset('img/statistic.svg')}}" alt="" />
                        </div>
                        <div class="p-4 m-4">
                            <div class="sm:text-center md:text-center lg:text-center">
                                <h1 class="text-4xl tracking-tight font-bold text-gray-900 sm:text-5xl md:text-6xl">
                                    <span class="block xl:inline">¡Lleve su negocio</span>
                                    <span class="block text-upvent xl:inline">a las nubes!</span>
                                </h1>
                                <p class="block xl:inline mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                                    ¿Sabía que solo el 35% de las empresas Mexicanas están en la nube?
                                    <br />
                                    Conformada por un grupo de programadores, entusiastas y expertos en diversas
                                    áreas de tecnología, nos encargamos de llevar a las pequeñas, medianas y
                                    grandes empresas un paso más allá en el mundo de la tecnología. Con una amplia
                                    gama de productos y servicios de código libre cien porciento comprometido con
                                    la libertad y la ética profesional.
                                </p>
                            </div>
                            <a href="" class="bg-upvent rounded-lg text-sm font-bold text-white text-center px-4 py-3 transition duration-300 ease-in-out hover:bg-blue-600 mr-6">
                                Ir al MarketCloud <i class="ml-1 bi bi-bag-fill"></i>
                            </a>
                        </div>

                    </div>


                    <!-- Footer -->
                    @include('includes.footer')

                    <!-- Scripts -->
                    <script src="/js/app.js" type="text/javascript"></script>
    </body>
</html>
