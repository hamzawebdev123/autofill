<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Form extends Model
{
    protected $fillable = ['first_name','last_name','work_email','password','password_confirmation'];
}
