<?php

use Illuminate\Support\Facades\Route;
use App\Http\Livewire\Frontpage;

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

/* Log-in required routes
 * Admin routes might change on deploy CI/CD to prevent bruteforce
 * or other attacks
 *
 * if you are using this for your own purposes make sure to subsitute the
 * dashboard name with your preffered route name */

Route::group(['middleware' => [
    'auth:sanctum',
    'verified',
    'accessrole'
]], function () {

    /* Route for the main dashboard */

    Route::get('/dashboard', function() {
        return view('dashboard');
    })->name('dashboard');


    /* Route for the pages editor */

    Route::get('/pages', function() {
        return view('admin.pages');
    })->name('pages');

    /* Route for the navigation menus */

    Route::get('/navigation-menus', function() {
        return view('admin.navigation-menus');
    })->name('navigation-menus');

});

Route::get('/{urlslug}', Frontpage::class);
Route::get('/', Frontpage::class);
