<?php

namespace App\Http\Controllers;

use App\Models\Form;
use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Illuminate\Support\Facades\Log;

class UserController extends Controller
{
    public function showForm()
    {
        $formEntries = Form::all();
        return view('form',get_defined_vars());
    }
    public function auto()
    {
        return view('auto');
    }
    public function submitForm(Request $request)
    {
       $form = Form::create([
        'first_name' => $request->first_name,
        'last_name' => $request->last_name,
        'work_email' => $request->work_email,
        'password' => $request->password,
        'password_confirmation' => $request->password_confirmation,
       ]);
       return redirect()->back()->with('success','submitted successfully');
    }



    public function trigger($id)
    {
        $data = Form::findOrFail($id);

        $first = escapeshellarg($data->first_name);
        $last = escapeshellarg($data->last_name);
        $email = escapeshellarg($data->work_email);
        $pass = escapeshellarg($data->password);
        $confirm = escapeshellarg($data->password_confirmation);

        $command = "python D:\\github_kloud\\autofill\\bot.py $first $last $email $pass $confirm";

        // Execute command and capture output
        $output = shell_exec($command);

        // Log the output for debugging
        \Log::info("Selenium Output: " . $output);

        // You don't have $process here; shell_exec returns string or null, not a process object.
        // So remove process-related code or replace with Process if needed.

        return back()->with('success', 'Autofill triggered!');
    }

    // public function trigger($id)
    // {
    //     $data = Form::findOrFail($id);

    //     $first = escapeshellarg($data->first_name);
    //     $last = escapeshellarg($data->last_name);
    //     $email = escapeshellarg($data->work_email);
    //     $pass = escapeshellarg($data->password);
    //     $confirm = escapeshellarg($data->password_confirmation);

    //     $command = "python D:\\github_kloud\\autofill\\auto.py $first $last $email $pass $confirm";

    //     // Execute command and capture output
    //     $output = shell_exec($command);

    //     // Log the output for debugging
    //     \Log::info("Selenium Output: " . $output);

    //     // You don't have $process here; shell_exec returns string or null, not a process object.
    //     // So remove process-related code or replace with Process if needed.

    //     return back()->with('success', 'Autofill triggered!');
    // }
}
