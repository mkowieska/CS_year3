<?php
namespace App\Controller;

use App\Exception\NotFoundException;
use App\Model\MusicAlbum;
use App\Service\Router;
use App\Service\Templating;

class MusicAlbumController
{
    public function indexAction(Templating $templating, Router $router): ?string
    {
        $musicalbums = MusicAlbum::findAll();
        $html = $templating->render('musicalbum/index.html.php', [
            'musicalbums' => $musicalbums,
            'router' => $router,
        ]);
        return $html;
    }

    public function createAction(?array $musicalbums_request, Templating $templating, Router $router): ?string
    {
        if ($musicalbums_request) {
            $musicalbum = MusicAlbum::fromArray($musicalbums_request);
            // @todo missing validation
            $musicalbum->save();

            $path = $router->generatePath('musicalbum-index');
            $router->redirect($path);
            return null;
        } else {
            $musicalbum = new MusicAlbum();
        }

        $html = $templating->render('musicalbum/create.html.php', [
            'musicalbum' => $musicalbum,
            'router' => $router,
        ]);
        return $html;
    }

    public function editAction(int $musicalbums_id, ?array $musicalbums_request, Templating $templating, Router $router): ?string
    {
        $musicalbum = MusicAlbum::find($musicalbums_id);
        if (! $musicalbum) {
            throw new NotFoundException("Missing musicalbum with id $musicalbums_id");
        }

        if ($musicalbums_request) {
            $musicalbum->fill($musicalbums_request);
            // @todo missing validation
            $musicalbum->save();

            $path = $router->generatePath('musicalbum-index');
            $router->redirect($path);
            return null;
        }

        $html = $templating->render('musicalbum/edit.html.php', [
            'musicalbum' => $musicalbum,
            'router' => $router,
        ]);
        return $html;
    }

    public function showAction(int $musicalbums_id, Templating $templating, Router $router): ?string
    {
        $musicalbum = MusicAlbum::find($musicalbums_id);
        if (! $musicalbum) {
            throw new NotFoundException("Missing musicalbum with id $musicalbums_id");
        }

        $html = $templating->render('musicalbum/show.html.php', [
            'musicalbum' => $musicalbum,
            'router' => $router,
        ]);
        return $html;
    }

    public function deleteAction(int $musicalbums_id, Router $router): ?string
    {
        $musicalbum = MusicAlbum::find($musicalbums_id);
        if (! $musicalbum) {
            throw new NotFoundException("Missing musicalbum with id $musicalbums_id");
        }

        $musicalbum->delete();
        $path = $router->generatePath('musicalbum-index');
        $router->redirect($path);
        return null;
    }
}
