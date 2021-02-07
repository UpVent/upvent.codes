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

/* about us page route */
Route::get('/about', function() {
    return view('pages.about');
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
