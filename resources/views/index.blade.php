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
        <link rel="stylesheet" href="{{ asset('css/index.css') }}" type="text/css" media="screen" />

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




        <!-- Scripts -->
        <script src="/js/app.js" type="text/javascript"></script>
    </body>
</html>
