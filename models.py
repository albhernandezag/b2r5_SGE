# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class Equipo(models.Model):
    _name = 'equipo'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    ciudad = fields.Char(string='Ciudad')
    fecha_fundacion = fields.Date(string='Fecha de Fundación')
    jugadores = fields.One2many('jugador', 'equipo_id', string='Jugadores')


class Jugador(models.Model):
    _name = 'jugador'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    posicion = fields.Selection([('portero', 'Portero'),
                                 ('extremo derecho', 'Extremo Derecho'),
                                 ('lateral derecho', 'Lateral Derecho'),
                                 ('central', 'Central'),
                                 ('lateral izquierda', 'Lateral Izquierdo'),
                                 ('extremo izquierdo', 'Extremo Izquierdo'),
                                 ('pivote', 'Pivote')],
                                string='Posición')
    equipo_id = fields.Many2one('equipo', string='Equipo')
    '''
    media de jugadores por equipo
    '''
    @api.depends('equipo_id')
    def _compute_media_jugadores(self):
        for jugador in self:
            jugadores = jugador.equipo_id.jugadores
            if jugadores:
                jugador.media_jugadores = len(jugadores) / len(jugadores.mapped('equipo_id'))
            else:
                jugador.media_jugadores = 0

class Entrenador(models.Model):
    _name = 'entrenador'
    _inherit = 'jugador'
    _rec_name = 'entrenador'

    entrenador = fields.Boolean(string='Entrenador')
