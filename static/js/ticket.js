class PointTable // 描画用の色と座標を覚えるためのクラス
{
    constructor( _table_max = 2 ) {
        this.x = []
        this.move = []
        this.avg_move = 0
        this.table_max = _table_max
        for ( let i=0 ; i<_table_max ; i++ ) {
            this.x.push( 0 )
        }
    }

    get_idx( _i ) {
        const i = ( _i < 0 ? -_i : _i ) // abs
        return i % this.table_max
    }

    get_xy( _tc ) {
        const r = this.get_idx( _tc.identifier )
        return this.x[r]
    }

    set_xy( _tc ){
        const r = this.get_idx( _tc.identifier )
        this.x[r] = _tc.pageX
    }

    set_move( _tc ){
        const r = this.get_idx( _tc.identifier )
        this.move[r] = _tc.pageX - this.get_xy( _tc )
    }

    reset_move( _tc ){
        const r = this.get_idx( _tc.identifier )
        this.move[r] = 0
        this.avg_move = 0
        circle.style.left = rect_circle + "px"
    }
}

const xy_tbl = new PointTable()
const elm = document.querySelector( 'canvas#canvas' )
const circle = document.querySelector( 'div#child' )
const children = circle.children
var isPassed = false
const rect_circle = circle.offsetLeft
const ctx = elm.getContext( '2d' )
const for_touches = ( _evt, _fnc ) => {
    for ( let i=0 ; i<_evt.changedTouches.length ; i++ )
        _fnc( _evt.changedTouches[i] )
}

elm.addEventListener( "touchstart", ( _evt ) => {
    _evt.preventDefault()
    for_touches( _evt, ( _t ) => xy_tbl.set_xy( _t ) )
}, false )

elm.addEventListener( "touchmove", ( _evt ) => {
    _evt.preventDefault()
    for_touches( _evt, ( _t ) => xy_tbl.set_move( _t ) )
    if ( ( xy_tbl.move[1] - xy_tbl.move[0] ) < 30 && xy_tbl.move[0] > 0 && xy_tbl.move[1] > 0 && isPassed == false ) {
        xy_tbl.avg_move = ( xy_tbl.move[0] + xy_tbl.move[1] ) / 2
        circle.style.left = rect_circle + xy_tbl.avg_move + "px"
        if ( xy_tbl.avg_move > 400 ) {
            isPassed = true
        }
    }
}, false )

elm.addEventListener( "touchend", ( _evt ) => {
    _evt.preventDefault()
    for_touches( _evt, ( _t ) => xy_tbl.reset_move( _t ) )
    if ( isPassed == true ) {
        for ( let i=0 ; i<children.length ; i++ ) {
            children[i].style.backgroundColor = "red"
        }
    }
}, false )