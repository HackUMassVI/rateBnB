<!DOCTYPE html>
<style>
/* CSS used here will be applied after bootstrap.css */

body {
 background: url('${image}') no-repeat center center fixed;
 -webkit-background-size: cover;
 -moz-background-size: cover;
 -o-background-size: cover;
 background-size: cover;
}

.panel-default {
 opacity: 0.95;
 margin-top:30px;
}
.form-group.last {
 margin-bottom:0px;
}
</style>

<html lang="en">


  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <title>RateBnB Score</title>

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

  </head>
  <body>
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">RateBnB</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->
    </nav>
    <div class="container">
      <div class="container">
        <div class="row">
            <div class="col-md-4 col-md-offset-4">
                <div class="panel panel-default">
                    <div class="panel-body">
                      <h3 class="text-center">${listing_name}</h3>
                      <p class="text-center"><a href="${url}">Listing URL</a></p>
                        <div class="form-horizontal">
                        <div class="form-group text-center" style="margin-left: 15%">
                            <div class="col-sm-9">
                                <h2> Total Score<br>
                                  % if int(score[:2])>=80:
                                  <font color="green">&ensp; ${score}</font> 
                                  % elif int(score[:2])>=65:
                                  <font color="#9EFF00">&ensp; ${score}</font> 
                                  % elif int(score[:2])>40:
                                  <font color="#FFCD00">&ensp; ${score}</font> 
                                  % else:
                                  <font color="red">&ensp; ${score}</font> 
                                  % endif
                                </h2>

                            </div>
                            <div class="col-sm-9">
                            <div class="progress">
                              <div class="progress-bar bg-succes" role="progressbar" style="width: ${score[:2]}%" aria-valuenow="${score[:2]}" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                                
                            </div>
                            <div class="col-sm-9">
                                <h4> Safety Score: ${safety} </h4>
                            </div>
                            <div class="col-sm-9">
                                <h4> Num Reviews: ${review_count} </h4>
                            </div>
                            <div class="col-sm-9">
                                <h4> Amenitites: <br>
                                % for amen in amenities:
                                    ${amen}<br>
                                % endfor
                                </h4>
                            </div>
                            <div class="col-sm-9">
                                <h4> Rating: ${rating} </h4>
                            </div>
                        </div>
                      </div>
                    </div>
            </div>
        </div>
    </div>
  </div>
</div>

</body>
</html>
