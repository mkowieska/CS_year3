<?php
namespace App\Model;

use App\Service\Config;

class MusicAlbum
{
    private ?int $id = null;
    private ?string $subject = null;
    private ?string $content = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function setId(?int $id): MusicAlbum
    {
        $this->id = $id;

        return $this;
    }

    public function getSubject(): ?string
    {
        return $this->subject;
    }

    public function setSubject(?string $subject): MusicAlbum
    {
        $this->subject = $subject;

        return $this;
    }

    public function getContent(): ?string
    {
        return $this->content;
    }

    public function setContent(?string $content): MusicAlbum
    {
        $this->content = $content;

        return $this;
    }

    public static function fromArray($array): MusicAlbum
    {
        $musicalbum = new self();
        $musicalbum->fill($array);

        return $musicalbum;
    }

    public function fill($array): MusicAlbum
    {
        if (isset($array['id']) && ! $this->getId()) {
            $this->setId($array['id']);
        }
        if (isset($array['subject'])) {
            $this->setSubject($array['subject']);
        }
        if (isset($array['content'])) {
            $this->setContent($array['content']);
        }

        return $this;
    }

    public static function findAll(): array
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM musicalbum';
        $statement = $pdo->prepare($sql);
        $statement->execute();

        $musicalbums = [];
        $musicalbumsArray = $statement->fetchAll(\PDO::FETCH_ASSOC);
        foreach ($musicalbumsArray as $musicalbumsArray) {
            $musicalbums[] = self::fromArray($musicalbumsArray);
        }

        return $musicalbums;
    }

    public static function find($id): ?MusicAlbum
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM musicalbum WHERE id = :id';
        $statement = $pdo->prepare($sql);
        $statement->execute(['id' => $id]);

        $musicalbumsArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $musicalbumsArray) {
            return null;
        }
        $musicalbum = MusicAlbum::fromArray($musicalbumsArray);

        return $musicalbum;
    }

    public function save(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        if (! $this->getId()) {
            $sql = "INSERT INTO musicalbum (subject, content) VALUES (:subject, :content)";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                'subject' => $this->getSubject(),
                'content' => $this->getContent(),
            ]);

            $this->setId($pdo->lastInsertId());
        } else {
            $sql = "UPDATE musicalbum SET subject = :subject, content = :content WHERE id = :id";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                ':subject' => $this->getSubject(),
                ':content' => $this->getContent(),
                ':id' => $this->getId(),
            ]);
        }
    }

    public function delete(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = "DELETE FROM musicalbum WHERE id = :id";
        $statement = $pdo->prepare($sql);
        $statement->execute([
            ':id' => $this->getId(),
        ]);

        $this->setId(null);
        $this->setSubject(null);
        $this->setContent(null);
    }
}
