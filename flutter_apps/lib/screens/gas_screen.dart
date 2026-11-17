import 'package:flutter/material.dart';

/// «МойГаз» — утилитарный, «госуслужный» интерфейс: плоские секции без теней,
/// скругления 8, плотные строки-списки, сегмент-контрол и липкая кнопка снизу.
const _blue = Color(0xFF0B63CE);
const _ink = Color(0xFF1B1F27);
const _grey = Color(0xFF6B7280);
const _hair = Color(0xFFE2E6EC);
const _bg = Color(0xFFEDEFF3);

class GasScreen extends StatelessWidget {
  const GasScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: _bg,
      body: Column(
        children: [
          // системная шапка
          Container(
            color: _blue,
            padding: const EdgeInsets.fromLTRB(14, 10, 14, 12),
            child: SafeArea(
              bottom: false,
              child: Row(
                children: const [
                  Icon(Icons.arrow_back_rounded, color: Colors.white, size: 21),
                  SizedBox(width: 14),
                  Text('Лицевой счёт 4512 8830',
                      style: TextStyle(
                          fontSize: 15.5, color: Colors.white, fontWeight: FontWeight.w600)),
                  Spacer(),
                  Icon(Icons.help_outline_rounded, color: Colors.white, size: 20),
                ],
              ),
            ),
          ),
          // статусная полоса
          Container(
            width: double.infinity,
            color: const Color(0xFFFFF4D6),
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
            child: Row(
              children: const [
                Icon(Icons.info_outline_rounded, size: 15, color: Color(0xFF9A6B00)),
                SizedBox(width: 8),
                Text('Передайте показания до 25 октября',
                    style: TextStyle(fontSize: 12, color: Color(0xFF9A6B00))),
              ],
            ),
          ),
          Expanded(
            child: ListView(
              padding: const EdgeInsets.only(bottom: 8),
              physics: const NeverScrollableScrollPhysics(),
              children: [
                // сумма
                Container(
                  color: Colors.white,
                  padding: const EdgeInsets.fromLTRB(14, 14, 14, 14),
                  child: Row(
                    children: [
                      Container(width: 3, height: 54, color: _blue),
                      const SizedBox(width: 12),
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: const [
                          Text('НАЧИСЛЕНО ЗА ОКТЯБРЬ 2026',
                              style: TextStyle(
                                  fontSize: 9.5, letterSpacing: 0.8, color: _grey)),
                          SizedBox(height: 4),
                          Text('1 248,60 ₽',
                              style: TextStyle(
                                  fontSize: 29, fontWeight: FontWeight.w700, color: _ink)),
                        ],
                      ),
                      const Spacer(),
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: const [
                          Text('СРОК ОПЛАТЫ',
                              style: TextStyle(
                                  fontSize: 9.5, letterSpacing: 0.8, color: _grey)),
                          SizedBox(height: 4),
                          Text('10.11.2026',
                              style: TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w700,
                                  color: Color(0xFFCC3B2E))),
                        ],
                      ),
                    ],
                  ),
                ),
                const _Gap(),
                // сегмент-контрол
                Container(
                  color: Colors.white,
                  padding: const EdgeInsets.fromLTRB(14, 12, 14, 0),
                  child: Container(
                    height: 34,
                    decoration: BoxDecoration(
                        color: _bg, borderRadius: BorderRadius.circular(8)),
                    child: Row(
                      children: const [
                        _Seg('Показания', active: true),
                        _Seg('История'),
                        _Seg('Тарифы'),
                      ],
                    ),
                  ),
                ),
                // показания
                Container(
                  color: Colors.white,
                  padding: const EdgeInsets.fromLTRB(14, 14, 14, 14),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text('СЧЁТЧИК № 8831-220 · ПОСЛЕДНЕЕ 01279 м³',
                          style:
                              TextStyle(fontSize: 9.5, letterSpacing: 0.8, color: _grey)),
                      const SizedBox(height: 10),
                      Row(
                        children: [
                          for (var i = 0; i < 5; i++) ...[
                            Container(
                              width: 38,
                              height: 42,
                              alignment: Alignment.center,
                              decoration: BoxDecoration(
                                color: i >= 3 ? Colors.white : const Color(0xFFF6F7F9),
                                borderRadius: BorderRadius.circular(6),
                                border: Border.all(
                                    color: i >= 3 ? _blue : _hair, width: i >= 3 ? 1.6 : 1),
                              ),
                              child: Text('01284'[i],
                                  style: TextStyle(
                                      fontSize: 19,
                                      fontWeight: FontWeight.w700,
                                      color: i >= 3 ? _ink : _grey)),
                            ),
                            const SizedBox(width: 6),
                          ],
                          const Spacer(),
                          Container(
                            padding:
                                const EdgeInsets.symmetric(horizontal: 16, vertical: 11),
                            decoration: BoxDecoration(
                                color: _blue, borderRadius: BorderRadius.circular(8)),
                            child: const Text('Передать',
                                style: TextStyle(
                                    fontSize: 13,
                                    color: Colors.white,
                                    fontWeight: FontWeight.w600)),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
                const _Gap(),
                // таблица расхода
                Container(
                  color: Colors.white,
                  child: Column(
                    children: [
                      const Padding(
                        padding: EdgeInsets.fromLTRB(14, 12, 14, 8),
                        child: Row(
                          children: [
                            Text('РАСХОД ПО МЕСЯЦАМ',
                                style: TextStyle(
                                    fontSize: 9.5, letterSpacing: 0.8, color: _grey)),
                            Spacer(),
                            Text('м³ / ₽',
                                style: TextStyle(fontSize: 9.5, color: _grey)),
                          ],
                        ),
                      ),
                      const _Row('Октябрь 2026', '5', '1 248,60', last: false, accent: true),
                      const _Row('Сентябрь 2026', '4', '998,88'),
                      const _Row('Август 2026', '3', '749,16'),
                      const _Row('Июль 2026', '4', '998,88', last: true),
                    ],
                  ),
                ),
                const _Gap(),
                Container(
                  color: Colors.white,
                  child: Column(
                    children: const [
                      _Link('Квитанция за октябрь', Icons.description_outlined),
                      _Link('История платежей', Icons.history_rounded),
                      _Link('Заявка в службу газа', Icons.build_outlined, last: true),
                    ],
                  ),
                ),
              ],
            ),
          ),
          // липкая кнопка
          Container(
            padding: const EdgeInsets.fromLTRB(14, 10, 14, 14),
            decoration: const BoxDecoration(
              color: Colors.white,
              border: Border(top: BorderSide(color: _hair)),
            ),
            child: Row(
              children: [
                Expanded(
                  child: Container(
                    height: 46,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                        color: _blue, borderRadius: BorderRadius.circular(8)),
                    child: const Text('Оплатить 1 248,60 ₽',
                        style: TextStyle(
                            fontSize: 15,
                            color: Colors.white,
                            fontWeight: FontWeight.w600)),
                  ),
                ),
                const SizedBox(width: 10),
                Container(
                  width: 46,
                  height: 46,
                  decoration: BoxDecoration(
                      border: Border.all(color: _hair),
                      borderRadius: BorderRadius.circular(8)),
                  child: const Icon(Icons.qr_code_rounded, size: 22, color: _ink),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _Gap extends StatelessWidget {
  const _Gap();
  @override
  Widget build(BuildContext context) => const SizedBox(height: 8);
}

class _Seg extends StatelessWidget {
  const _Seg(this.label, {this.active = false});
  final String label;
  final bool active;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        margin: const EdgeInsets.all(3),
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: active ? Colors.white : Colors.transparent,
          borderRadius: BorderRadius.circular(6),
          boxShadow: active
              ? const [BoxShadow(color: Color(0x14000000), blurRadius: 4, offset: Offset(0, 1))]
              : null,
        ),
        child: Text(label,
            style: TextStyle(
                fontSize: 12.5,
                fontWeight: active ? FontWeight.w700 : FontWeight.w500,
                color: active ? _ink : _grey)),
      ),
    );
  }
}

class _Row extends StatelessWidget {
  const _Row(this.month, this.vol, this.sum, {this.last = false, this.accent = false});
  final String month;
  final String vol;
  final String sum;
  final bool last;
  final bool accent;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(14, 11, 14, 11),
      decoration: BoxDecoration(
        border: last ? null : const Border(bottom: BorderSide(color: _hair)),
      ),
      child: Row(
        children: [
          Text(month,
              style: TextStyle(
                  fontSize: 13.5,
                  color: _ink,
                  fontWeight: accent ? FontWeight.w700 : FontWeight.w500)),
          const Spacer(),
          SizedBox(
              width: 34,
              child: Text(vol,
                  textAlign: TextAlign.right,
                  style: const TextStyle(
                      fontSize: 13.5, color: _grey, fontWeight: FontWeight.w600))),
          const SizedBox(width: 16),
          SizedBox(
            width: 78,
            child: Text('$sum ₽',
                textAlign: TextAlign.right,
                style: TextStyle(
                    fontSize: 13.5,
                    color: accent ? _blue : _ink,
                    fontWeight: FontWeight.w700)),
          ),
        ],
      ),
    );
  }
}

class _Link extends StatelessWidget {
  const _Link(this.label, this.icon, {this.last = false});
  final String label;
  final IconData icon;
  final bool last;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(14, 13, 14, 13),
      decoration: BoxDecoration(
        border: last ? null : const Border(bottom: BorderSide(color: _hair)),
      ),
      child: Row(
        children: [
          Icon(icon, size: 19, color: _blue),
          const SizedBox(width: 12),
          Text(label, style: const TextStyle(fontSize: 14, color: _ink)),
          const Spacer(),
          const Icon(Icons.chevron_right_rounded, size: 20, color: _grey),
        ],
      ),
    );
  }
}
