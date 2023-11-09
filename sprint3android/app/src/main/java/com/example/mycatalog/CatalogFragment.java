package com.example.mycatalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class CatalogFragment extends Fragment {
    private Context context;


    public static CatalogFragment newInstance() {
        CatalogFragment frag = new CatalogFragment();
        return frag;
    }


    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        this.context = context;
    }


    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {


        View layout = inflater.inflate(R.layout.fragment_catalog, container, false);
        Button boton = layout.findViewById(R.id.navego);

        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (context != null) {
                    Intent myIntent = new Intent(context, DetailActivity.class);
                    context.startActivity(myIntent);
                }
            }
        });
      return layout;
    }
}