<template>
    <div class="container">
      <h1>Movies</h1>
      <div class="row">
        <div class="col-md-4" v-for="movie in movies" :key="movie.id">
          <div class="card mb-4">
            <img :src="movie.poster" class="card-img-top" alt="Movie Poster" />
            <div class="card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
              <p class="card-text">{{ movie.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue"
  
  let movies = ref([])
  
  function fetchMovies() {
    fetch("/api/v1/movies")
      .then(res => res.json())
      .then(data => {
        movies.value = data.movies
      })
      .catch(err => console.log(err))
  }
  
  onMounted(() => {
    fetchMovies()
  })
  </script>