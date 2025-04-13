<template>
    <div>
      <h1>Upload Form</h1>
  
      <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
      <div v-if="errors.length" class="alert alert-danger">
        <p v-for="error in errors" :key="error">{{ error }}</p>
      </div>
  
      <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
        <div>
          <label for="title">Movie Title:</label>
          <input type="text" name="title" required>
        </div>
        <div>
          <label for="description">Description:</label>
          <textarea name="description" required></textarea>
        </div>
        <div>
          <label for="poster">Poster:</label>
          <input type="file" name="poster" accept="image/*" required>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  let csrf_token = ref("");
  let successMessage = ref("");
  let errors = ref([]);
  
  function getCsrfToken() {
    fetch('/api/v1/csrf-token')
      .then(res => res.json())
      .then(data => {
        csrf_token.value = data.csrf_token;
      });
  }
  
  function saveMovie() {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
  
    fetch("/api/v1/movies", {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.message) {
        successMessage.value = data.message;
        errors.value = [];
      } else if (data.errors) {
        successMessage.value = "";
        errors.value = data.errors;
      }
    })
    .catch(error => {
      console.error("Error:", error);
    });
  }
  
  onMounted(() => {
    getCsrfToken();
  });
  </script>
  
  <style src="../assets/movie.css"></style>