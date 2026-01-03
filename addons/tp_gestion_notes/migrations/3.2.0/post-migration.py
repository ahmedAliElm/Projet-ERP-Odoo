# -*- coding: utf-8 -*-

def migrate(cr, version):
    """
    Migration pour ajouter les nouveaux champs priority, is_favorite, date_echeance
    """
    # Vérifier si les colonnes existent déjà
    cr.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name='tp_note_interne' AND column_name='priority'
    """)
    
    if not cr.fetchone():
        # Ajouter la colonne priority
        cr.execute("""
            ALTER TABLE tp_note_interne 
            ADD COLUMN priority VARCHAR
        """)
        # Définir la valeur par défaut pour les enregistrements existants
        cr.execute("""
            UPDATE tp_note_interne 
            SET priority = '1' 
            WHERE priority IS NULL
        """)
    
    # Vérifier et ajouter is_favorite
    cr.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name='tp_note_interne' AND column_name='is_favorite'
    """)
    
    if not cr.fetchone():
        cr.execute("""
            ALTER TABLE tp_note_interne 
            ADD COLUMN is_favorite BOOLEAN DEFAULT FALSE
        """)
    
    # Vérifier et ajouter date_echeance
    cr.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name='tp_note_interne' AND column_name='date_echeance'
    """)
    
    if not cr.fetchone():
        cr.execute("""
            ALTER TABLE tp_note_interne 
            ADD COLUMN date_echeance DATE
        """)
    
    # Créer les index pour améliorer les performances
    try:
        cr.execute("CREATE INDEX IF NOT EXISTS tp_note_interne_priority_idx ON tp_note_interne(priority)")
    except:
        pass
    
    try:
        cr.execute("CREATE INDEX IF NOT EXISTS tp_note_interne_is_favorite_idx ON tp_note_interne(is_favorite)")
    except:
        pass
    
    try:
        cr.execute("CREATE INDEX IF NOT EXISTS tp_note_interne_date_echeance_idx ON tp_note_interne(date_echeance)")
    except:
        pass

