package com.example.renova

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class Hidroeletrica : AppCompatActivity() {
    lateinit var Bt_proximo : Button
    lateinit var Bt_menu : Button
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_hidroeletrica)
        Bt_proximo = findViewById(R.id.Bt_proximo)
        Bt_proximo.setOnClickListener {
            Goto_prox()
        }

        Bt_menu = findViewById(R.id.Bt_menu)
        Bt_menu.setOnClickListener {
            var vai_menu = Intent(this,MainActivity::class.java)
            startActivity(vai_menu)

        }
    }
    fun Goto_prox(){
        var vai_solar = Intent(this,Solar::class.java)
        startActivity(vai_solar)
    }
}