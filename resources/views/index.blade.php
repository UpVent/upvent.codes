<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>{{config('app.name', 'UpVent')}} - Soluciones en la nube para tu negocio. Low Cost, Siempre Listas.</title>

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

                        <a class="block text-black rounded-lg bg-white shadow-lg p-2 mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-blue mr-4 rounded focus:outline-none focus:shadow-outline" href="#">
                            Inicio
                        </a>

                        <a href="{{ url('/blog') }}" class=" block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Blog
                        </a>

                        <a href="{{ url('/about') }}" class=" block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Nosotros
                        </a>

                        <a href="{{ url('/services') }}" class=" block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Servicios
                        </a>

                        <a href="{{ url('/contact') }}" class=" block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
                            Contacto
                        </a>

                        <a href="{{ url('/marketcloud') }}" class="block mt-4 lg:inline-block lg:mt-0 text-teal-lighter hover:text-white mr-4 rounded focus:outline-none focus:shadow-outline">
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
                    <div class="grid grid-cols-2 gap-4 sm:hidden md:inline-flex lg:inline-flex">
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
                                </p>
                                <p class="block xl:inline mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                                    Conformada por un grupo de programadores, entusiastas y expertos en diversas
                                    áreas de tecnología, nos encargamos de llevar a las pequeñas, medianas y
                                    grandes empresas un paso más allá en el mundo de la tecnología. Con una amplia
                                    gama de productos y servicios de código libre cien porciento comprometido con
                                    la libertad y la ética profesional.
                                </p>
                            </div>
                            <a href="{{ url('/marketcloud') }}" class="bg-upvent rounded-lg text-sm font-bold text-white text-center px-4 py-3 transition duration-300 ease-in-out hover:bg-blue-600 mr-6">
                                Ir al MarketCloud <i class="ml-1 bi bi-bag-fill"></i>
                            </a>
                        </div>
                    </div>

                    <div class="container mx-auto">
                        <hr />
                    </div>

                    <!-- Second features section -->
                    <div class="py-12 bg-white">
                        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                            <div class="lg:text-center">
                                <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
                                    Concéntrese en lo importante para usted.
                                </p>
                                <p class="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
                                    No tendrá que preocuparse por la infraestructura, la disponibilidad o desarrollo. Podrá dedicar el cien por ciento del tiempo a su negocio y a sus clientes.
                                </p>
                            </div>

                            <div class="mt-10">
                                <dl class="space-y-10 md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10">
                                    <div class="flex">
                                        <div class="flex-shrink-0">
                                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white shadow">
                                                <i class="text-base bi bi-tools"></i>
                                            </div>
                                        </div>
                                        <div class="ml-4">
                                            <dt class="text-lg leading-6 font-medium text-gray-900">
                                                Soluciones Personalizadas
                                            </dt>
                                            <dd class="mt-2 text-base text-gray-500">
                                                Elija lo que usted desea en sus soluciones. Desde blogs hasta plataformas empresariales, todo es posible con nosotros.
                                            </dd>
                                        </div>
                                    </div>

                                    <div class="flex">
                                        <div class="flex-shrink-0">
                                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white shadow">
                                                <i class="text-base bi bi-clipboard-check"></i>
                                            </div>
                                        </div>
                                        <div class="ml-4">
                                            <dt class="text-lg leading-6 font-medium text-gray-900">
                                                ¡Todo lo necesario!
                                            </dt>
                                            <dd class="mt-2 text-base text-gray-500">
                                                Contamos con un equipo de desarrolladores altamente experimentado, nuestros expertos le ayudarán a expandir su negocio de forma exponencial.
                                            </dd>
                                        </div>
                                    </div>

                                    <div class="flex">
                                        <div class="flex-shrink-0">
                                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white shadow">
                                                <i class="text-base bi bi-cash-stack"></i>
                                            </div>
                                        </div>
                                        <div class="ml-4">
                                            <dt class="text-lg leading-6 font-medium text-gray-900">
                                                Precios Accesibles
                                            </dt>
                                            <dd class="mt-2 text-base text-gray-500">
                                                Escale su negocio cuando lo desee, en UpVent los precios se adaptan a usted y no al revés. Disfrute del poder de la nube a su propio ritmo.
                                            </dd>
                                        </div>
                                    </div>

                                    <div class="flex">
                                        <div class="flex-shrink-0">
                                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white shadow">
                                                <i class="text-base bi bi-person-square"></i>
                                            </div>
                                        </div>
                                        <div class="ml-4">
                                            <dt class="text-lg leading-6 font-medium text-gray-900">
                                                Tratos personales / empresariales
                                            </dt>
                                            <dd class="mt-2 text-base text-gray-500">
                                                El trato de UpVent es universal. Si usted desea crear una idea para usted mismo o para su empresa puede acudir con nosotros. Siempre a su servicio.
                                            </dd>
                                        </div>
                                    </div>
                                </dl>
                            </div>
                        </div>
                    </div>


                    <!-- Client banner -->

                    <div class="m-8 container mx-auto">
                        <p class="mt-4 max-w-2xl text-3xl text-gray-500 lg:mx-auto">Nuestros clientes hablan por nosotros</p>
                        <p class="mt-4 max-w-2xl text-sm text-gray-500 lg:mx-auto">Conozca las opiniones de los clientes más exitosos que tenemos. Ellos confían a UpVent su computación en la nube.</p>
                    </div>

                    <div class="grid sm:grid-cols-2 sm:gap-2 md:grid-cols-4 md:gap-4 lg:grid-cols-4 lg:gap-2">
                        <div class="m-2 p-2">
                            <!-- component -->
                            <div class="max-w-sm bg-white shadow-lg rounded-lg overflow-hidden my-4">
                                <img class="w-full h-56 object-cover object-center" src="{{asset('img/aacosta.jpg')}}" alt="avatar">
                                <div class="flex items-center px-6 py-3 bg-upvent">
                                    <i class="text-md bi bi-newspaper text-white"></i>
                                    <h1 class="mx-3 text-white font-semibold text-lg">Informando</h1>
                                </div>
                                <div class="py-4 px-6">
                                    <h1 class="text-2xl font-semibold text-gray-800">Armando A.</h1>
                                    <p class="py-2 text-lg text-gray-700">
                                        Amo que sea una empresa mexicana, además de que son jóvenes y super claros en los temas que no todos dominamos. Agradezco de sobremanera su apoyo y pues mi hosting será con ustedes por un buen rato. Saludos
                                        PD. En 24 horas estuvo listo mi sitio 🤯
                                    </p>
                                    <div class="flex items-center mt-4 text-gray-700">
                                        <i class="text-sm bi bi-briefcase-fill"></i>
                                        <h1 class="px-2 text-sm">Periodista Independiente</h1>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="m-2 p-2">
                            <div class="max-w-sm bg-white shadow-lg rounded-lg overflow-hidden my-4">
                                <img class="w-full h-56 object-cover object-center" src="{{asset('img/asmith.jpg')}}" alt="avatar">
                                <div class="flex items-center px-6 py-3 bg-upvent">
                                    <i class="text-md bi bi-lightbulb text-white"></i>
                                    <h1 class="mx-3 text-white font-semibold text-lg">Innovando</h1>
                                </div>
                                <div class="py-4 px-6">
                                    <h1 class="text-2xl font-semibold text-gray-800">Anthony S.</h1>
                                    <p class="py-2 text-lg text-gray-700">
                                        "Inicié mi negocio de tecnología con muy poco tiempo entre manos y con poco dinero, ahora gracias a UpVent mi negocio a día de hoy se encuentra en línea las 24 horas del día, los 7 días de la semana.Recomiendo ampliamente sus servicios"
                                    </p>
                                    <div class="flex items-center mt-4 text-gray-700">
                                        <i class="text-sm bi bi-briefcase-fill"></i>
                                        <h1 class="px-2 text-sm">CEO - CyberIndustree</h1>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="m-2 p-2">
                            <div class="max-w-sm bg-white shadow-lg rounded-lg overflow-hidden my-4">
                                <img class="w-full h-56 object-cover object-center" src="{{asset('img/rturanzas.jpg')}}" alt="avatar">
                                <div class="flex items-center px-6 py-3 bg-upvent">
                                    <i class="text-md bi bi-brush hover text-white"></i>
                                    <h1 class="mx-3 text-white font-semibold text-lg">Creando</h1>
                                </div>
                                <div class="py-4 px-6">
                                    <h1 class="text-2xl font-semibold text-gray-800">Regina T.</h1>
                                    <p class="py-2 text-lg text-gray-700">
                                        "Soy una chica que quiere compartir su arte y también poder venderlo y mostrarlo al mundo. La atención que te dan es fenomenal y las personas que la componen también lo son. Estoy muy feliz con el resultado, totalmente recomendada."
                                    </p>
                                    <div class="flex items-center mt-4 text-gray-700">
                                        <i class="text-sm bi bi-briefcase-fill"></i>
                                        <h1 class="px-2 text-sm">Artista Digital</h1>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="m-2 p-2">
                            <div class="max-w-sm bg-white shadow-lg rounded-lg overflow-hidden my-4">
                                <img class="w-full h-56 object-cover object-center" src="{{asset('img/opurata.jpeg')}}" alt="avatar">
                                <div class="flex items-center px-6 py-3 bg-upvent">
                                    <i class="text-md bi bi-star text-white"></i>
                                    <h1 class="mx-3 text-white font-semibold text-lg">Mejorando</h1>
                                </div>
                                <div class="py-4 px-6">
                                    <h1 class="text-2xl font-semibold text-gray-800">Jair S.</h1>
                                    <p class="py-2 text-lg text-gray-700">
                                        "Súper-recomendable! Muy buen dominio de las herramientas necesarias y te ofrece alternativas para lograr lo que le solicitas. Excelente!"
                                    </p>
                                    <div class="flex items-center mt-4 text-gray-700">
                                        <i class="text-sm bi bi-briefcase-fill"></i>
                                        <h1 class="px-2 text-sm">CEO - Mide Mejora y Gana</h1>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <hr />

                    <!-- Sección de Beneficios -->

                    <div class="max-w-screen-xl p-4 bg-white dark:bg-gray-800 mx-auto px-4 sm:px-6 lg:px-8 relative py-26 lg:mt-20">
                        <div class="relative">
                            <div class="lg:grid lg:grid-flow-row-dense lg:grid-cols-2 lg:gap-8 lg:items-center">
                                <div class="lg:col-start-2 lg:max-w-2xl ml-auto">
                                    <h4 class="mt-2 text-2xl leading-8 font-extrabold text-gray-900 dark:text-white sm:text-3xl sm:leading-9">
                                        Beneficios con UpVent
                                    </h4>
                                    <p class="mt-4 text-lg leading-6 text-gray-500 dark:text-gray-300">
                                        Hay un gran número de razones por las cuales UpVent es una empresa de calidad y grandes valores. Aquí les presentaremos las más importantes.
                                    </p>
                                    <ul class="mt-8 md:grid md:grid-cols-2 gap-6">
                                        <li class="mt-6 lg:mt-0">
                                            <div class="flex">
                                                <span class="flex-shrink-0 flex items-center justify-center h-6 w-6 rounded-full bg-blue-100 text-green-800 dark:text-green-500 drark:bg-transparent">
                                                    <svg class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                                        <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd">
                                                        </path>
                                                    </svg>
                                                </span>
                                                <span class="ml-4 text-base leading-6 font-medium text-gray-500 dark:text-gray-200">
                                                    Low Cost
                                                </span>
                                            </div>
                                        </li>
                                        <li class="mt-6 lg:mt-0">
                                            <div class="flex">
                                                <span class="flex-shrink-0 flex items-center justify-center h-6 w-6 rounded-full bg-blue-100 text-green-800 dark:text-green-500 drark:bg-transparent">
                                                    <svg class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                                        <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd">
                                                        </path>
                                                    </svg>
                                                </span>
                                                <span class="ml-4 text-base leading-6 font-medium text-gray-500 dark:text-gray-200">
                                                    Libre y Open Source
                                                </span>
                                            </div>
                                        </li>
                                        <li class="mt-6 lg:mt-0">
                                            <div class="flex">
                                                <span class="flex-shrink-0 flex items-center justify-center h-6 w-6 rounded-full bg-blue-100 text-green-800 dark:text-green-500 drark:bg-transparent">
                                                    <svg class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                                        <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd">
                                                        </path>
                                                    </svg>
                                                </span>
                                                <span class="ml-4 text-base leading-6 font-medium text-gray-500 dark:text-gray-200">
                                                    Educativo
                                                </span>
                                            </div>
                                        </li>
                                        <li class="mt-6 lg:mt-0">
                                            <div class="flex">
                                                <span class="flex-shrink-0 flex items-center justify-center h-6 w-6 rounded-full bg-blue-100 text-green-800 dark:text-green-500 drark:bg-transparent">
                                                    <svg class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                                        <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd">
                                                        </path>
                                                    </svg>
                                                </span>
                                                <span class="ml-4 text-base leading-6 font-medium text-gray-500 dark:text-gray-200">
                                                    Innovador
                                                </span>
                                            </div>
                                        </li>
                                    </ul>
                                    <div class="m-8 p-4 container mx-auto">
                                        <a class="p-4 bg-upvent hover:bg-blue-600 text-white font-bold border-black rounded-lg shadow-lg">Comenzar con UpVent <i class="ml-2 mr-2 mb-2 bi bi-trophy-fill"></i></a>
                                    </div>
                                </div>
                                <div class="mt-10 lg:-mx-4 relative relative-20 lg:mt-0 lg:col-start-1">
                                    <div class="relative space-y-4">
                                        <div class="flex items-end justify-center lg:justify-start space-x-4">
                                            <img class="rounded-lg shadow-lg w-32 md:w-56" width="200" src="{{ asset('img/benefits/coins.jpg') }}" alt="1"/>
                                            <img class="rounded-lg shadow-lg w-40 md:w-64" width="260" src="{{ asset('img/benefits/libre.jpg') }}" alt="2"/>
                                        </div>
                                        <div class="flex items-start justify-center lg:justify-start space-x-4 ml-12">
                                            <img class="rounded-lg shadow-lg w-24 md:w-40" width="170" src="{{ asset('img/benefits/innovation.jpg') }}" alt="3"/>
                                            <img class="rounded-lg shadow-lg w-32 md:w-56" width="200" src="{{ asset('img/benefits/library.jpg') }}" alt="4"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Footer -->
                    @include('includes.footer')

                    <!-- Scripts -->
                    <script src="/js/app.js" type="text/javascript"></script>
    </body>
</html>
