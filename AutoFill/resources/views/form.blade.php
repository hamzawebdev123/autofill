<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    <div class="container mt-5">
        <h2 class="mb-4">Fill the Form</h2>

        <form method="POST" action="{{ route('form.submit') }}" class="row g-3">
          @csrf

          <div class="col-md-6">
            <input type="text" name="first_name" class="form-control" placeholder="First Name" required>
          </div>

          <div class="col-md-6">
            <input type="text" name="last_name" class="form-control" placeholder="Last Name" required>
          </div>

          <div class="col-md-12">
            <input type="email" name="work_email" class="form-control" placeholder="Email" required>
          </div>

          <div class="col-md-6">
            <input type="password" name="password" class="form-control" placeholder="Password" required>
          </div>

          <div class="col-md-6">
            <input type="password" name="password_confirmation" class="form-control" placeholder="Confirm Password" required>
          </div>

          <div class="col-12">
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </form>

        <hr class="my-5">

        <h3>Saved Form Entries</h3>
        <table class="table table-bordered table-hover mt-3">
          <thead class="table-dark">
            <tr>
              <th>First Name</th>
              <th>Email</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            @foreach($formEntries as $entry)
            <tr>
              <td>{{ $entry->first_name }}</td>
              <td>{{ $entry->work_email }}</td>
              <td>
                <form method="POST" action="{{ route('autofill.trigger', $entry->id) }}">
                  @csrf
                  <button type="submit" class="btn btn-success btn-sm">Autofill</button>
                </form>
              </td>
            </tr>
            @endforeach
          </tbody>
        </table>
      </div>
</body>
</html>
