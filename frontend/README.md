# Sprout Exam - Frontend

## Env File

```sh
VITE_BASE_API_URL=http://localhost:8080
```

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Project Setup With Docker

### Build Docker Image

```sh
docker build -t sprout-frontend .
```

### Run Docker Image

```sh
docker run -p 80:80 sprout-frontend:latest
```