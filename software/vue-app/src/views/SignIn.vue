<template>
  <v-container fill-height>
    <v-row justify="center" align="center">
      <!-- <v-col cols="12" sm="4">
        Centered both vertically and horizontally
      </v-col> -->
      <v-form ref="form" v-model="valid" lazy-validation>
        <h1>Sign In to your account</h1>
        <v-text-field
          v-model="username"
          :rules="usernameRules"
          label="username"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="passwordRules"
          :type="show1 ? 'text' : 'password'"
          name="input-10-1"
          label="password"
          hint="At least 5 characters"
          counter
          @click:append="show1 = !show1"
        ></v-text-field>

        <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          @click="validate"
        >
          Sign In
        </v-btn>
        <router-link to="/signup">Sign Up</router-link>
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    show1: false,
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