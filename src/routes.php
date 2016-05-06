<?php
// Routes

$app->get('/', function () {
    // Sample log message
    $this->logger->info("Slim-Skeleton '/' route");

    // Render index view
    return $this->renderer->render('index');
});
