<?php

namespace App\Service;

use App\Exception\NotFoundException;

class Router
{
    public function dispatch(): void
    {
        // Pobierz nazwę akcji z URL
        $action = $_GET['action'] ?? 'index'; // Domyślna akcja to "index"

        // Rozdzielenie akcji na kontroler i metodę
        [$controllerName, $methodName] = $this->parseAction($action);

        // Wygenerowanie pełnej nazwy klasy kontrolera
        $controllerClass = "App\\Controller\\{$controllerName}";

        // Sprawdzenie, czy kontroler istnieje
        if (!class_exists($controllerClass)) {
            throw new NotFoundException("Controller '$controllerClass' not found");
        }

        // Tworzenie instancji kontrolera
        $controller = new $controllerClass(new Config(), new Templating());

        // Sprawdzenie, czy metoda istnieje w kontrolerze
        if (!method_exists($controller, $methodName)) {
            throw new NotFoundException("Method '$methodName' not found in controller '$controllerClass'");
        }

        // Wywołanie metody kontrolera
        $controller->$methodName();
    }

    private function parseAction(string $action): array
    {
        // Rozdziel "Controller@method" na [Controller, method]
        if (strpos($action, '@') !== false) {
            return explode('@', $action);
        }

        // Domyślnie użyj kontrolera "PostController" i akcji "indexAction"
        return ['PostController', 'indexAction'];
    }

    public function generatePath(string $action, ?array $params = []): string
    {
        $query = $action ? http_build_query(array_merge(['action' => $action], $params)) : null;
        $path = "/index.php" . ($query ? "?$query" : null);
        return $path;
    }

    public function redirect($path): void
    {
        header("Location: $path");
    }
}
