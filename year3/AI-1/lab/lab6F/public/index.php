<?php
//require_once __DIR__ . '/../vendor/autoload.php';
//
//use App\Service\Config;
//use App\Service\Router;
//
//$config = new Config();
//$router = new Router($config);
//$router->dispatch();
//
//$action = $_REQUEST['action'] ?? null;
//switch ($action) {
//    case 'post-index':
//    case null:
//        $controller = new \App\Controller\PostController();
//        $view = $controller->indexAction($templating, $router);
//        break;
//    case 'post-create':
//        $controller = new \App\Controller\PostController();
//        $view = $controller->createAction($_REQUEST['post'] ?? null, $templating, $router);
//        break;
//    case 'post-edit':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\PostController();
//        $view = $controller->editAction($_REQUEST['id'], $_REQUEST['post'] ?? null, $templating, $router);
//        break;
//    case 'post-show':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\PostController();
//        $view = $controller->showAction($_REQUEST['id'], $templating, $router);
//        break;
//    case 'post-delete':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\PostController();
//        $view = $controller->deleteAction($_REQUEST['id'], $router);
//        break;
//    case 'info':
//        $controller = new \App\Controller\InfoController();
//        $view = $controller->infoAction();
//        break;
//    default:
//        $view = 'Not found';
//        break;
//}
//
//if ($view) {
//    echo $view;
//}

use App\Service\Config;
use App\Service\Router;

$config = new Config();
$router = new Router();

try {
    $router->dispatch();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
spl_autoload_register(function ($class) {
    $prefix = 'App\\';
    $base_dir = __DIR__ . '/../src/';

    $len = strlen($prefix);
    if (strncmp($prefix, $class, $len) !== 0) {
        return;
    }

    $relative_class = substr($class, $len);
    $file = $base_dir . str_replace('\\', '/', $relative_class) . '.php';

    if (file_exists($file)) {
        require $file;
    }
});
