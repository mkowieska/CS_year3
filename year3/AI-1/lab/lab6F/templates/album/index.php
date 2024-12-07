<h1>Album List</h1>
<ul>
    <?php foreach ($albums as $album): ?>
        <li>
            <a href="/albums/show/<?= $album->getId() ?>"><?= $album->getTitle() ?></a>
            <form action="/albums/delete/<?= $album->getId() ?>" method="post" style="display:inline;">
                <button type="submit">Delete</button>
            </form>
        </li>
    <?php endforeach; ?>
</ul>
<a href="/albums/create">Add New Album</a>
