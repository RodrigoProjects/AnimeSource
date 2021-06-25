<template
  ><main class="profile-page">
    <Headerings :photo="header" tipe="Results" />
    <Lister :tipe="tipe" :result="result" />
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
      result: this.$route.params.id,
      header:
        "https://i.pinimg.com/originals/59/ca/ff/59caffae11062ce14bd4d5141da3caba.jpg",
      tipe: "Search",
    };
  },
};
</script>
