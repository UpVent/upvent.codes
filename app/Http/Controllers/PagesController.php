<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PagesController extends Controller
{
    public function index() {
        $title = "Nube Inteligente.";

        return view('pages.index') -> with('title', $title);
    }


    public function about() {
        $title = "Nosotros.";

        return view('pages.about') -> with('title', $title);
    }

    public function services() {

        $data = array(
          'title' => 'Servicios.',
          'services' => ['Programación', 'Infraestructura', 'Consultoría']
        );

        return view('pages.services') -> with($data);
    }

}
