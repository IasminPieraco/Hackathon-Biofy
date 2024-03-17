package com.example.renova

import android.content.Intent
import android.os.Bundle
import android.service.voice.VoiceInteractionSession.ActivityId
import android.view.View.OnClickListener
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.github.kittinunf.fuel.httpGet


class MainActivity : AppCompatActivity() {
    lateinit var Bt_Solar : Button
    lateinit var Bt_Eolica : Button
    lateinit var Bt_Biomassa : Button
    lateinit var Bt_Hidro : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val requisicao = Request(Method.GET, "https://xkcd.com/info.0.json")
        val cliente: HttpHandler = JavaHttpClient()
        val respostaRequisicao = cliente(requisicao)

        println(respostaRequisicao)

        Bt_Solar = findViewById(R.id.Bt_Solar)
        Bt_Solar.setOnClickListener {
            GotoSolar()
        }

        Bt_Biomassa = findViewById(R.id.Bt_Biomassa)
        Bt_Biomassa.setOnClickListener {
            GotoBio()
        }

        Bt_Eolica = findViewById(R.id.Bt_Eolica)
        Bt_Eolica.setOnClickListener {
            GotoEolica()
        }

        Bt_Hidro = findViewById(R.id.Bt_Hidro)
        Bt_Hidro.setOnClickListener {
            GotoHidro()
        }
    }
    fun GotoSolar(){
        var vai_solar = Intent(this,Solar::class.java)
        startActivity(vai_solar)
    }
    fun GotoBio(){
        var vai_bio = Intent(this,Biomassa::class.java)
        startActivity(vai_bio)
    }
    fun GotoHidro(){
        var vai_Hidro = Intent(this,Hidroeletrica::class.java)
        startActivity(vai_Hidro)
    }
    fun GotoEolica(){
        var vai_eolica = Intent(this,Eolica::class.java)
        startActivity(vai_eolica)
    }
}