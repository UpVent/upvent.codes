<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>{{config('app.name', 'UpVent')}} - Soluciones en la nube para tu negocio. Low Cost, Siempre Listas.</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&family=Roboto&display=swap" rel="stylesheet">

        <!-- Favicon -->
        <link rel="shortcut icon" href="{{ asset('img/favicon.ico') }}">

        <!-- Styles -->
        <link rel="stylesheet" href="/css/app.css" type="text/css" media="screen" />

    </head>
    <body class="antialiased font-montserrat">
        <!-- This example requires Tailwind CSS v2.0+ -->
        <div>
            <nav class="flex items-center justify-between flex-wrap bg-upvent shadow-inner p-6">
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
            </nav>
        </div>


        <!-- Scripts -->
        <script src="/js/app.js" type="text/javascript"></script>
    </body>
</html>
