<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;

// Route::get('/', function () {
//     return view('welcome');
// });
Route::get('/', [UserController::class, 'showForm'])->name('form');
Route::post('/form/submit', [UserController::class, 'submitForm'])->name('form.submit');
Route::post('/autofill/{id}', [UserController::class, 'trigger'])->name('autofill.trigger');
Route::get('/auto', [UserController::class, 'auto'])->name('auto');
