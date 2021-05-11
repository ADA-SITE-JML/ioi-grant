<template>
  <v-container fill-height>
    <v-row justify="center" align="center">
      <!-- <v-col cols="12" sm="4">
        Centered both vertically and horizontally
      </v-col> -->
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="username"
          :rules="usernameRules"
          label="username"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :rules="passwordRules"
          label="password"
          required
        ></v-text-field>

        <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          @click="validate"
        >
          Submit
        </v-btn>
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    username: "",
    usernameRules: [
      (v) => !!v || "username is required",
      (v) => (v && v.length >= 3) || "Name must be greater than 2 characters",
    ],
    password: "",
    passwordRules: [
      (v) => !!v || "password is required",
      (v) => (v && v.length >= 5) || "Name must be greater than 5 characters",
    ],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
};
</script>