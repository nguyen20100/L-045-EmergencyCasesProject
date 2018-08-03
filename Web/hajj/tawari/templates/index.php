
<!DOCTYPE html>
<html lang="en">
<head>
  <title>طوارئ</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <link rel="stylesheet" type="text/css" href="index.css">



</head>
<body>

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-6 col-md-8 col-xs-12 left">
    
    </div>
    <div class="col-sm-6 col-md-4 col-xs-12 right">
      <form class="Login" method="POST">
        <div class="form-group">
          <label for="Email1">Email address</label>
          <input name="Email" type="email" class="form-control" id="Email1" placeholder="Enter email" required>
        </div>
        <div class="form-group">
          <label for="Password1">Password</label>
          <input name="Password1" type="password" class="form-control" id="Password1" placeholder="Password" required>
        </div>
        <div class="form-group form-check">
          <label class="form-check-label " id="p" for="Check1">Remember me</label>
          <input name="Check1" type="checkbox" class="form-check-input" id="Check1">
        </div>
        <button type="submit" id="Login" class="btn btn-lg btn-danger LogIn">LogIn</button>
      </form>
    </div>
  </div>
</div>
</body>
</html>