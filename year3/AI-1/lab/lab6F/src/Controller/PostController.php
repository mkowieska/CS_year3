<?php
namespace App\Controller;

use App\Service\Config;
use App\Service\Templating;
use App\Service\Router;

class PostController
{
//    private $config;
//    private $templating;
//    private $router;
//
//    public function __construct(Config $config, Templating $templating, Router $router)
//    {
//        $this->config = $config;
//        $this->templating = $templating;
//        $this->router = $router;
//    }
//
//    // Akcja listy albumów
//    public function indexAction()
//    {
//        $albums = $this->config->getDb()->query("SELECT * FROM albums")->fetchAll(\PDO::FETCH_CLASS, Album::class);
//        echo $this->templating->render('post/index.php', ['albums' => $albums]);
//    }
//
//    // Akcja szczegółowego widoku albumu
//    public function showAction($id)
//    {
//        $stmt = $this->config->getDb()->prepare("SELECT * FROM albums WHERE id = :id");
//        $stmt->execute(['id' => $id]);
//        $album = $stmt->fetchObject(Album::class);
//
//        if (!$album) {
//            throw new \Exception("Album not found!");
//        }
//
//        echo $this->templating->render('post/show.php', ['post' => $album]);
//    }
//
//    // Akcja tworzenia nowego albumu
//    public function createAction()
//    {
//        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
//            $stmt = $this->config->getDb()->prepare("INSERT INTO albums (title, artist, release_date) VALUES (:title, :artist, :release_date)");
//            $stmt->execute([
//                'title' => $_POST['title'],
//                'artist' => $_POST['artist'],
//                'release_date' => $_POST['release_date']
//            ]);
//            $this->router->redirect('/albums');
//        }
//
//        echo $this->templating->render('post/create.php');
//    }
//
//    // Akcja edycji albumu
//    public function editAction($id)
//    {
//        $stmt = $this->config->getDb()->prepare("SELECT * FROM albums WHERE id = :id");
//        $stmt->execute(['id' => $id]);
//        $album = $stmt->fetchObject(Album::class);
//
//        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
//            $stmt = $this->config->getDb()->prepare("UPDATE albums SET title = :title, artist = :artist, release_date = :release_date WHERE id = :id");
//            $stmt->execute([
//                'id' => $id,
//                'title' => $_POST['title'],
//                'artist' => $_POST['artist'],
//                'release_date' => $_POST['release_date']
//            ]);
//            $this->router->redirect('/albums');
//        }
//
//        echo $this->templating->render('post/edit.php', ['post' => $album]);
//    }
//
//    // Akcja kasowania albumu
//    public function deleteAction($id)
//    {
//        $stmt = $this->config->getDb()->prepare("DELETE FROM albums WHERE id = :id");
//        $stmt->execute(['id' => $id]);
//        $this->router->redirect('/albums');
//    }\
    private $config;
    private $templating;

    public function __construct(Config $config, Templating $templating)
    {
        $this->config = $config;
        $this->templating = $templating;
    }

    public function indexAction()
    {
        echo "PostController is working!";
    }
}
