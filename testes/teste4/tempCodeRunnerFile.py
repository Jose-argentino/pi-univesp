
    # Verifica se a conexão foi criada e a fecha corretamente
    if conn and conn.is_connected():
        conn.close()
        print("Conexão fechada.")
