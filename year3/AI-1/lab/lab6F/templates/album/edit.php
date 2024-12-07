<h1>Edit Album</h1>
<form action="" method="post">
    <label>Title: <input type="text" name="title" value="<?= $album->getTitle() ?>"></label><br>
    <label>Artist: <input type="text" name="artist" value="<?= $album->getArtist() ?>"></label><br>
    <label>Release Date: <input type="date" name="release_date" value="<?= $album->getReleaseDate() ?>"></label><br>
    <button type="submit">Save</button>
</form>
<a href="/albums">Back to list</a>
