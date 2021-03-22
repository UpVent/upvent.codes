<div class="divide-y divide-blue-800" x-data="{ show: false }">
    <nav class="flex items-center bg-upvent p-6 shadow-lg">
        {{-- Menu hidden --}}
        <div class="block h-8 mr-3 sm:hidden">
            <button @click="show =! show"
                class="block items-center px-3 py-2 border text-white border-white hover:text-gray hover:border-gray rounded focus:outline-none focus:shadow-outline">
                <svg class="fill-current h-6 w-6" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path x-show="!show" d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                    <path x-show="show" fill-rule="evenodd" d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z"/>
                </svg>

            </button>
        </div>

        {{-- Navbar Logo --}}
        <div class="w-full h-12 flex items-center">
            <img class="object-center object-contain h-10 w-auto" src="{{asset('img/logo-white.png')}}" alt="UpVent White Logo" />
        </div>

        {{-- Menu shown --}}
        <div class="flex justify-end sm:w-8/12">

            {{-- Top Navigation --}}
            <ul class="hidden sm:flex sm:text-left text-white text-sm">
                <a href="https://facebook.com/UpVentMX">
                    <li class="cursor-pointer px-4 py-2"><i class="bi bi-facebook"></i></li>
                </a>
                <a href="https://instagram.com/upventmx">
                    <li class="cursor-pointer px-4 py-2"><i class="bi bi-instagram"></i></li>
                </a>
                <a href="https://github.com/UpVent">
                    <li class="cursor-pointer px-4 py-2"><i class="bi bi-github"></i></li>
                </a>
                <a href="{{ url('/login') }}">
                    <li class="cursor-pointer px-4 py-2 hover:underline">Login</li>
                </a>
            </ul>
        </div>
    </nav>
    <div class="sm:flex sm:min-h-screen">
        <aside class="bg-upvent text-white sm:w-4/12 md:w-3/12 lg:w-2/12 divide-y divide-white divide-dashed">
            {{-- Desktop Web View --}}
            <ul class="hidden text-white text-sm sm:block sm:text-left">
                @foreach ($sideBarLinks as $item)
                    <a href="{{ url('/'.$item->slug) }}">
                        <li class="cursor-pointer px-4 py-2 hover:bg-blue-700">{{ $item->label }}</li>
                    </a>
                @endforeach
            </ul>

            {{-- Mobile Web View --}}
            <div :class="show ? 'block' : 'hidden'" class="pb-3 divide-y divide-white block sm:hidden">
                <ul class="text-sm">
                    @foreach ($topNavLinks as $item)
                        <a href="{{ url('/'.$item->slug) }}">
                            <li class="cursor-pointer px-4 py-2 hover:bg-blue-700">{{ $item->label }}</li>
                        </a>
                    @endforeach
                </ul>

                {{-- Top Navigation Mobile Web View --}}
                <ul class="text-sm">
                    <a href="{{ url('/login') }}">
                        <li class="cursor-pointer px-4 py-2 hover:bg-blue-700">login</li>
                    </a>
                </ul>

            </div>
        </aside>
        <main class="bg-gray-100 p-12 min-h-screen sm:w-8/12 md:w-9/12 lg:w-10/12">
            <section class="divide-y text-gray-900">
                <h1 class="text-3xl font-bold">{{ $title }}</h1>
            </section>
            <article class="mt-5 font-bold">
                <div class="mt-5 text-sm">
                    {!! $content !!}
                </div>
            </article>
        </main>
    </div>
</div>
