@extends('layouts.app')

@section('content')
    <h1>
        {{$title}}
    </h1>
    <p>Conozca la amplia variedad de servicios que UpVent puede ofrecerle a usted y a su empresa.</p>

    @if(count($services) > 0)
        <ul>
            @foreach($services as $service)
                <li>{{$service}}</li>
            @endforeach
        </ul>
    @endif

@endsection
