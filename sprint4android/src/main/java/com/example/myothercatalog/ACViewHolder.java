package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.content.Context;
import android.content.Intent;
import android.widget.Button;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class ACViewHolder extends RecyclerView.ViewHolder{
    // Aquí nos encontramos los elementos de la vista de la celda
    private TextView name;
    private ImageView game;
    private Button button;

    // Este constructor recibe la vista de la celda e inicializa los atributos con los elementos de la misma.
    public ACViewHolder(@NonNull View ivi) {
        super(ivi);
        name = ivi.findViewById(R.id.text_view_game);
        game = ivi.findViewById(R.id.image_view_game);
        button = ivi.findViewById(R.id.button);
    }
    // Y en este último método se muestran los datos en la vista de la celda:
    public void showData(ACData acData) {
        name.setText(acData.getName());
        Util.downloadBitmapToImageView(acData.getImage_url(), this.game); // Empleamos una utilidad para descargar y establecer la imagen del juego en el ImageView.
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = v.getContext();

                Intent intent = new Intent(context, DetailActivity.class);

                context.startActivity(intent);
            }
        });
    }
}