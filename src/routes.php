<?php
// Routes

$app->get('/', function () {
    // Sample log message
    $this->logger->info("Slim-Skeleton '/' route");

    // Render index view
    return $this->renderer->render('index');
});

// Administrator router

// Administrator homepage
$app->get('/admin', function() {
    return $this->renderer->render('admin/index');
});


// User management
$app->get('/admin/user', function(){
    return $this->renderer->render('/admin/user');
});
