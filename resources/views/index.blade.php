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
    <body class="antialiased">
        <!-- This example requires Tailwind CSS v2.0+ -->
        <div>
            <nav class="bg-upvent shadow-inner">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex items-center justify-between h-16">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <img class="h-8 w-13 object-fill" src="{{asset('img/logo-white.png')}}" alt="Workflow">
                            </div>
                            <div class="hidden sm:block">
                                <div class="ml-10 flex items-baseline space-x-4">
                                    <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                                    <a href="#" class="shadow-xl bg-white text-purple px-3 py-2 rounded-md text-sm font-medium">Inicio</a>

                                    <a href="#" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Blog</a>

                                    <a href="#" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Nosotros</a>

                                    <a href="#" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Servicios</a>

                                    <a href="#" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Contacto</a>

                                    <a href="#" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Marketcloud</a>
                                </div>
                            </div>


                            @if (Route::has('login'))
                                <div class="hidden fixed top-0 right-0 px-6 py-4 sm:block">
                                    @auth
                                    <a href="{{ url('/dashboard') }}" class="text-sm text-gray-700 underline">Dashboard</a>
                            @else
                                    <a href="{{ route('login') }}" class="text-sm text-gray-700 underline">Login</a>

                                    @if (Route::has('register'))
                                        <a href="{{ route('register') }}" class="ml-4 text-sm text-gray-700 underline">Register</a>
                                    @endif
                                    @endauth
                                </div>
                            @endif

                            <div class="max-w-6xl mx-auto sm:px-6 lg:px-8">
                                <div class="mt-8 bg-white dark:bg-gray-800 overflow-hidden shadow sm:rounded-lg">

                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </nav>

            <main>
                <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
                    <!-- Replace with your content -->
                    <div class="px-4 py-6 sm:px-0">
                        <div class="border-4 border-dashed border-gray-200 rounded-lg h-96"></div>
                    </div>
                    <!-- /End replace -->
                </div>
            </main>
        </div>

    </body>
</html>
