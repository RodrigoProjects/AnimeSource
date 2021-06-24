<template>
  <main class="profile-page">
    <Headerings :photo="header" :tipe="tipe + 's'" />
    <Lister :tipe="tipe" />
  </main>
</template>

<script>
import Headerings from "../components/Headerings.vue";
import Lister from "../components/Listing.vue";
export default {
  components: {
    Headerings: Headerings,
    Lister: Lister,
  },
  data() {
    return {
      header:
        "https://i.pinimg.com/originals/a5/67/e0/a567e0483c452fd2c3a10a029edab41d.jpg",
      tipe: "Studio",
    };
  },
};
</script>

<style></style>
