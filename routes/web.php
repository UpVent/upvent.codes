<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

/* Public accessible routes */

/* Main page route */
Route::get('/', function () {
    return view('index');
});

/* Blog page route */


/* About page route */
Route::get('/about', function() {
    return view('pages.about');
});


/* Services page route */
Route::get('/services', function() {
    return view('pages.services');
});


/* Contact page route */
Route::get('/contact', function() {
    return view('pages.contact');
});


/* Marketcloud page route */
Route::get('/marketcloud', function() {
    return view('pages.marketcloud');
});


/* Privacy Policy page route */
Route::get('/privacy-policy', function() {
    return view('pages.privacy-policy');
});


/* Free software route */
Route::get('/open-source', function() {
    return view('pages.open-source');
});


/* Licenses page route */
Route::get('/licenses', function() {
    return view('pages.licenses');
});


/* Events page route */
Route::get('/events', function() {
    return view('pages.events');
});


/* Team page route */
Route::get('/team', function() {
    return view('pages.team');
});


/* Allies page route */
Route::get('/allies', function() {
    return view('pages.allies');
});


/* Log-in required routes
 * Admin routes might change on deploy CI/CD to prevent bruteforce
 * or other attacks
 *
 * if you are using this for your own purposes make sure to subsitute the
 * dashboard name with your preffered route name */
Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth'])->name('dashboard');

require __DIR__.'/auth.php';
