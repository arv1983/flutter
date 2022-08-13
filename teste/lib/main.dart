import 'package:flutter/material.dart';

main() =>  runApp(const TesteApp());


class TesteApp extends StatelessWidget {
const TesteApp({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('teste'),
        ),
        body: Column(
          children: [
            Text('1'),
            ElevatedButton(onPressed: () { print('clicou'); },
            child: Text('botao'),

            )
          ],
        )
            
          
        ),
      
      
    );
  }
}