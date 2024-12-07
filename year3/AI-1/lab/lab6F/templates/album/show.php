<h1><?= $album->getTitle() ?></h1>
<p>Artist: <?= $album->getArtist() ?></p>
<p>Release Date: <?= $album->getReleaseDate() ?></p>
<a href="/albums/edit/<?= $album->getId() ?>">Edit</a>
<a href="/albums">Back to list</a>
