package main

import (
    "net/http"

    "github.com/dimiro1/health"
)

func main() {

    handler := health.NewHandler()
    http.Handle("/health/", handler)
    http.ListenAndServe(":8080", nil)

}
