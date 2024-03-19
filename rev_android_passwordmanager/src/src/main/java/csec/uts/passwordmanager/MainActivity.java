package csec.uts.passwordmanager;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.content.Intent;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    public EditText inputted_password;
    public String password = "try harder lmao";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        inputted_password = findViewById(R.id.passwordInput);
    }

    public void confirmClicked(View v) {
        String input = inputted_password.getText().toString();
        if (input.equals(password)) {
            Intent intent = new Intent(this, LoggedIn.class);
            startActivity(intent);
        } else {
            Toast.makeText(this, "WRONG ❌❌❌❌", Toast.LENGTH_SHORT).show();
        }
    }
}