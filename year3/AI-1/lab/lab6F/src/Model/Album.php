<?php
namespace App\Model;

class Album
{
    private ?int $id = null;
    private string $title;
    private string $artist;
    private string $release_date;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getTitle(): string
    {
        return $this->title;
    }

    public function setTitle(string $title): void
    {
        $this->title = $title;
    }

    public function getArtist(): string
    {
        return $this->artist;
    }

    public function setArtist(string $artist): void
    {
        $this->artist = $artist;
    }

    public function getReleaseDate(): string
    {
        return $this->release_date;
    }

    public function setReleaseDate(string $release_date): void
    {
        $this->release_date = $release_date;
    }
}
